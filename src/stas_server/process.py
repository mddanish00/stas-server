import pythonmonkey as pm
import regex as re

pm.eval('const g=new Intl.Segmenter("ja-JP",{granularity:"sentence"});')

split_jp = pm.eval("text=>Array.from(g.segment(text)).map(s=>s.segment);")

newline_regex = re.compile(r"(\n+)")


def split_sentences_in_batch(text_list: list[str]):
    final_text_list: list[str] = []
    text_map: list[int] = []

    for text in text_list:
        split_text_list = [str(i) for i in split_jp(text)]
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
    is_bracket = text.endswith("」") and text.startswith("「")
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

    if is_bracket:
        text = f'"{text}"'

    return text


def remove_in_text(pattern_list: list[re.Pattern[str] | str], text: str):
    for p in pattern_list:
        text = re.sub(p, "", text)

    return text


def strip_bracket(text: str):
    return remove_in_text(
        [r"^「", r"^”", r"^“", r'^"', r"^'", r"」$", r"“$", r"”$", r'"$', r"'$"], text
    )


def pre_clean(text: str):
    text = text.strip()
    text = text.strip("﻿")
    return text


def post_clean(text: str):
    text: str = text.strip("﻿")
    text = re.sub(r"{", "", text, 0)
    text = re.sub(r"⁇ unk>", "<unk>", text)
    text = re.sub(r"”,", ",", text)
    text = re.sub(r"”\?", "?", text)
    text = text.strip()

    text = strip_bracket(text)
    text = text.strip()

    text = remove_in_text(
        [r"�", r"カ$", r"987$", r"^:", r"⁇", r"❛", r"^,", r"^-"], text
    )
    text = text.strip()

    if len(text) != 0:
        text = text[0].upper() + text[1:]

    return text
