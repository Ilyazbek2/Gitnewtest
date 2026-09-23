"""Task: merge all overlapping closed intervals."""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return sorted intervals after merging overlaps."""
    if not intervals:
        return []

    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return [(start, end) for start, end in merged]


if __name__ == "__main__":
    assert merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12)]) == [
        (1, 6),
        (8, 12),
    ]
    assert merge_intervals([]) == []
    print(merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12)]))
