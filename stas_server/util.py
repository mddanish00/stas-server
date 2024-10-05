from functools import _CacheInfo, lru_cache
from typing import Any, Callable, Literal, ParamSpec, TypeVar

def process_raw_string(text: str):
    return text.replace(r'\n', '\n')


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


# Based on solution of this question on StackOverflow
# https://stackoverflow.com/a/73517775
def hash_list(li: list) -> int:
    __hash = 0
    for i, e in enumerate(li):
        __hash = hash((__hash, i, hash_item(e)))
    return __hash


def hash_item(e) -> int:
    if hasattr(e, "__hash__") and callable(e.__hash__):
        try:
            return hash(e)
        except TypeError:
            pass
    if isinstance(e, (list, set, tuple)):
        return hash_list(list(e))
    else:
        raise TypeError(f"unhashable type: {e.__class__}")


PT = ParamSpec("PT")
RT = TypeVar("RT")


def lru_cache_ext(
    *opts, hashfunc: Callable[..., int] = hash_item, **kwopts
) -> Callable[[Callable[PT, RT]], Callable[PT, RT]]:
    def decorator(func: Callable[PT, RT]) -> Callable[PT, RT]:
        class _lru_cache_ext_wrapper:
            args: tuple
            kwargs: dict[str, Any]

            def cache_info(self) -> _CacheInfo: ...
            def cache_clear(self) -> None: ...

            @classmethod
            @lru_cache(*opts, **kwopts)
            def cached_func(cls, args_hash: int) -> RT:
                return func(*cls.args, **cls.kwargs)

            @classmethod
            def __call__(cls, *args: PT.args, **kwargs: PT.kwargs) -> RT:
                if kwargs.get("enable_cache"):
                    kwargs.pop("enable_cache")
                    __hash = hashfunc(
                        (
                            id(func),
                            *[hashfunc(a) for a in args],
                            *[(hashfunc(k), hashfunc(v)) for k, v in kwargs.items()],
                        )
                    )

                    cls.args = args
                    cls.kwargs = kwargs

                    cls.cache_info = cls.cached_func.cache_info
                    cls.cache_clear = cls.cached_func.cache_clear

                    return cls.cached_func(__hash)
                else:
                    kwargs.pop("enable_cache")
                    return func(*args, **kwargs)

        return _lru_cache_ext_wrapper()

    return decorator
