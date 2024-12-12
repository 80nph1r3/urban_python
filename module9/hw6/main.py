from typing import Generator


def all_variants(text: str) -> Generator[str, None, None]:
    substr_len = 1
    slice_start = -1
    slice_end = 0
    while substr_len <= len(text):
        while slice_end < len(text):
            slice_start += 1
            slice_end += 1
            yield text[slice_start:slice_end]
        substr_len += 1
        slice_start = -1
        slice_end = substr_len - 1


if __name__ == "__main__":
    a = all_variants("abc")

    for i in a:
        print(i)
