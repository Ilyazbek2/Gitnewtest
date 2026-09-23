"""Task: compress consecutive equal characters."""


def compress_string(text: str) -> str:
    """Return runs as character plus count, omitting a count of one."""
    if not text:
        return ""

    compressed: list[str] = []
    run_start = 0

    for index in range(1, len(text) + 1):
        if index == len(text) or text[index] != text[run_start]:
            count = index - run_start
            compressed.append(text[run_start])
            if count > 1:
                compressed.append(str(count))
            run_start = index

    result = "".join(compressed)
    return result if len(result) < len(text) else text


if __name__ == "__main__":
    assert compress_string("aaabbc") == "a3b2c"
    assert compress_string("abcd") == "abcd"
    print(compress_string("aaabbc"))