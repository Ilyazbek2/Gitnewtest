"""Task: find two indices whose values add up to target."""


def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    """Return the first pair of indices with the required sum."""
    seen: dict[int, int] = {}

    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return seen[complement], index
        seen[number] = index

    return None


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([1, 2, 3], 10) is None
    print(two_sum([2, 7, 11, 15], 9))