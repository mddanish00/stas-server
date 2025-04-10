from icu import Locale, BreakIterator
import regex as re

from stas_server.util import lru_cache_ext

locale = Locale("ja_JP")
break_iterator = BreakIterator.createSentenceInstance(locale)


def split_jp_core(text: str):
    break_iterator.setText(text)
    segmented_sentences: list[str] = []
    last_pos = 0
    for current_pos in break_iterator:
        sentence = text[last_pos:current_pos].strip()
        if sentence:
            segmented_sentences.append(sentence)
        last_pos = current_pos

    return segmented_sentences


newline_regex = re.compile(r"(\n+)")


split_jp = lru_cache_ext(maxsize=None)(split_jp_core)


def split_sentences_in_batch(text_list: list[str], enable_cache: bool):
    final_text_list: list[str] = []
    text_map: list[int] = []

    for text in text_list:
        split_text_list = [str(i) for i in split_jp(text, enable_cache=enable_cache)]
        final_text_list.extend(split_text_list)
        text_map.append(len(split_text_list))

    return final_text_list, text_map


def split_newlines(text: str):
    return [r for r in newline_regex.split(text) if r]


def check_if_not_newline(text: str) -> bool:
    """
    Check if the input string is not equal to newline.
    """
    return newline_regex.fullmatch(text) is None


def join_sentences_in_batch(text_list: list[str], text_map: list[int]):
    final_text_list: list[str] = []
    current_pointer = 0
    for count in text_map:
        aim_pointer: int = current_pointer + count
        tmp_text_list: list[str] = []

        while current_pointer < aim_pointer:
            tmp_text_list.append(text_list[current_pointer])
            current_pointer = current_pointer + 1

        filtered = filter(lambda t: t != "", tmp_text_list)
        final_text_list.append(" ".join(list(filtered)))

    return final_text_list


def get_original_state(text: str):
    is_bracket = (text.endswith("」") and text.startswith("「")) or (
        text.endswith("』") and text.startswith("『")
    )
    is_period = text.endswith("。")
    return is_bracket, is_period


def restore_original_state(text: str, is_bracket: bool, is_period: bool):
    if (
        not text.endswith(".")
        and not text.endswith("?")
        and not text.endswith("!")
        and is_period
    ):
        text = f"{text}."

    if is_bracket and not (
        (text.startswith("“") or text.startswith('"'))
        and (text.endswith('"') or text.endswith("”"))
    ):
        text = f'"{text}"'

    return text


def remove_in_text(pattern_list: list[re.Pattern[str] | str], text: str):
    for p in pattern_list:
        text = re.sub(p, "", text)

    return text


def strip_bracket(text: str):
    return remove_in_text(
        [
            r"^「",
            r"^”",
            r"^“",
            r'^"',
            r"^'",
            r"」$",
            r"“$",
            r"”$",
            r'"$',
            r"'$",
            r"^「",
            r"」$",
            r"^『",
            r"』$",
        ],
        text,
    )


def pre_clean(text: str):
    text = text.strip()
    text = text.strip("﻿")
    text = re.sub(r"、$", "", text)
    return text


def post_clean(text: str):
    text: str = text.strip("﻿")
    text = re.sub(r"{", "", text, 0)
    text = re.sub(r"⁇ unk>", "<unk>", text)
    text = re.sub(r"”,", ",", text)
    text = re.sub(r"”\?", "?", text)
    text = text.strip()

    if (text.startswith("“") or text.startswith('"')) and (
        text.endswith('"') or text.endswith("”")
    ):
        text = strip_bracket(text)

    text = text.strip()

    text = remove_in_text(
        [r"�", r"カ$", r"987$", r"^:", r"⁇", r"❛", r"^,", r"^-"], text
    )
    text = text.strip()

    if len(text) != 0:
        text = text[0].upper() + text[1:]

    return text
