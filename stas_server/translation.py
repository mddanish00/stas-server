import logging
import os
import time
from pathlib import Path
from typing import Pattern

import regex as re
import sentencepiece as spm
from ctranslate2 import Translator

from stas_server.util import (
    lru_cache_ext,
    split_list_by_condition,
    flatten_2d_list,
    recombine_split_list,
    deflate_flat_list,
)
from stas_server.process import (
    get_original_state,
    post_clean,
    restore_original_state,
    split_sentences_in_batch,
    join_sentences_in_batch,
    pre_clean,
    strip_bracket,
    split_newlines,
    check_if_not_newline,
)

log_translation = logging.getLogger("Translation")

# Paths
ct2_model_dir_path = Path("ct2Model")
sp_source_model_path = Path("spmModels", "spm.ja.nopretok.model")
sp_target_model_path = Path("spmModels", "spm.en.nopretok.model")

translator: Translator | None = None
spe = spm.SentencePieceProcessor()
spd = spm.SentencePieceProcessor()
jp_regex: Pattern[str] = re.compile(
    r"([\p{InCJKUnifiedIdeographs}\p{InCJKSymbolsandPunctuation}\p{InHiragana}\p{InKatakana}]+)"
)


def check_if_japanese_in_string(text: str) -> bool:
    return jp_regex.search(text) is not None


def setup_translation(cuda: bool = False, models_dir: str = "models"):
    global translator, spe, spd

    models_dir_path = Path(models_dir)
    spe.LoadFromFile((models_dir_path / sp_source_model_path).absolute().__str__())
    spd.LoadFromFile((models_dir_path / sp_target_model_path).absolute().__str__())

    if cuda is True:
        device = "cuda"
        compute_type = "default"
        inter_threads = os.cpu_count()
        intra_threads = 0
    else:
        device = "cpu"
        compute_type = "auto"
        inter_threads = 32
        intra_threads = 1

    translator = Translator(
        model_path=(models_dir_path / ct2_model_dir_path).absolute().__str__(),
        device=device,
        inter_threads=inter_threads,
        intra_threads=intra_threads,
        compute_type=compute_type,
    )


@lru_cache_ext(maxsize=None)
def core_translator(text_list: list[str]):
    text_list = spe.Encode(text_list, out_type=str)
    result = translator.translate_batch(
        source=text_list,
        beam_size=5,
        num_hypotheses=1,
        no_repeat_ngram_size=3,
    )
    return [str(spd.Decode(result[i].hypotheses[0])) for i in range(len(result))]


def common_translator(batch_content: list[str], enable_cache: bool):
    batch_content = [pre_clean(c) for c in batch_content]
    original_whole_state_list = [get_original_state(c) for c in batch_content]
    batch_content = [
        strip_bracket(c) if original_whole_state_list[i][0] else c
        for i, c in enumerate(batch_content)
    ]
    in_queue_list, in_queue_map = split_sentences_in_batch(batch_content, enable_cache)

    if len(in_queue_list) > 1:
        log_translation.info(f"Text In Queue: {in_queue_list}")
        in_queue_state = [get_original_state(q) for q in in_queue_list]
        in_queue_list = [
            strip_bracket(c) if in_queue_state[i][0] else c
            for i, c in enumerate(in_queue_list)
        ]
        result_list = core_translator(in_queue_list, enable_cache=enable_cache)
        log_translation.info(f"Result In Queue: {result_list}")
        result_list = [post_clean(r) for r in result_list]
        result_list = [
            restore_original_state(r, in_queue_state[i][0], in_queue_state[i][1])
            for i, r in enumerate(result_list)
        ]
        result_list = join_sentences_in_batch(result_list, in_queue_map)
        result_list = [
            restore_original_state(
                r, original_whole_state_list[i][0], original_whole_state_list[i][1]
            )
            for i, r in enumerate(result_list)
        ]
    else:
        result_list = core_translator(in_queue_list, enable_cache=enable_cache)
        result_list = [post_clean(result_list[0])]
        result = restore_original_state(
            result_list[0],
            original_whole_state_list[0][0],
            original_whole_state_list[0][1],
        )
        result_list = [result]

    return result_list


def translate(content: str, enable_cache: bool):
    log_translation.info(f"Text: {content}")
    start = time.time()

    batch_content, leftover, list_index_newline = split_list_by_condition(
        split_newlines(content), check_if_not_newline
    )
    result_list = common_translator(batch_content, enable_cache)
    result_list = recombine_split_list(result_list, leftover, list_index_newline)
    result = "".join(result_list)

    end = time.time()
    log_translation.info(f"Translation: {result}")
    log_translation.info(f"Time taken: {round(end - start, 2)}s")

    return result


def translate_batch(content: list[str], enable_cache: bool):
    batch_size = len(content)
    for i, t in enumerate(content):
        log_translation.info(f"Text Batch {i + 1} of {batch_size}: {t}")
    start = time.time()

    batch_content_2d = [split_newlines(c) for c in content]
    batch_content, list_index_2d = flatten_2d_list(batch_content_2d)
    batch_content, leftover, list_index_newline = split_list_by_condition(
        batch_content, check_if_not_newline
    )
    result_list = common_translator(batch_content, enable_cache)
    result_list = recombine_split_list(result_list, leftover, list_index_newline)
    result_list_2d = deflate_flat_list(result_list, list_index_2d)
    result_list = ["".join(r) for r in result_list_2d]

    end = time.time()
    for i, t in enumerate(result_list):
        log_translation.info(f"Translation Batch {i + 1} of {batch_size}: {t}")
    log_translation.info(f"Time taken: {round(end - start, 2)}s")

    return result_list
