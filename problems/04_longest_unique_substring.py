"""Task: find the length of the longest substring without repeated characters."""


def longest_unique_substring(text: str) -> int:
    """Return the maximum length of a substring with unique characters."""
    last_seen: dict[str, int] = {}
    window_start = 0
    longest = 0

    for index, character in enumerate(text):
        if character in last_seen and last_seen[character] >= window_start:
            window_start = last_seen[character] + 1
        last_seen[character] = index
        longest = max(longest, index - window_start + 1)

    return longest


if __name__ == "__main__":
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    print(longest_unique_substring("pwwkew"))