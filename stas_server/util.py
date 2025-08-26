import asyncio
from typing import Callable, Awaitable, Literal


def process_raw_string(text: str):
    return text.replace(r"\n", "\n")


def split_list_by_condition[T](obj_list: list[T], condition: Callable[[T], bool]):
    split_list: list[T] = []
    leftover_list: list[T] = []
    list_index: list[Literal["D", "L"]] = []

    for o in obj_list:
        if condition(o):
            split_list.append(o)
            list_index.append("D")
        else:
            leftover_list.append(o)
            list_index.append("L")

    return split_list, leftover_list, list_index


async def split_list_by_async_condition[T](
    obj_list: list[T], condition: Callable[[T], Awaitable[bool]]
):
    split_list: list[T] = []
    leftover_list: list[T] = []
    list_index: list[Literal["D", "L"]] = []

    tasks = [condition(o) for o in obj_list]
    results = await asyncio.gather(*tasks)

    for i, o in enumerate(obj_list):
        if results[i]:
            split_list.append(o)
            list_index.append("D")
        else:
            leftover_list.append(o)
            list_index.append("L")

    return split_list, leftover_list, list_index


def recombine_split_list[T](
    split_list: list[T], leftover_list: list[T], list_index: list[Literal["D", "L"]]
):
    return [split_list.pop(0) if i == "D" else leftover_list.pop(0) for i in list_index]


def flatten_2d_list[T](obj_2d_list: list[list[T]]):
    flat_list: list[T] = []
    list_index: list[int] = []
    for obj_list in obj_2d_list:
        list_index.append(len(obj_list))
        flat_list += obj_list

    return flat_list, list_index


def deflate_flat_list[T](flat_list: list[T], list_index: list[int]):
    deflate_list: list[list[T]] = []
    current_pointer = 0
    for item in list_index:
        deflate_list.append(flat_list[current_pointer : current_pointer + item])
        current_pointer += item

    return deflate_list
