"""Task: check whether brackets are correctly nested and closed."""


def is_valid_parentheses(text: str) -> bool:
    """Return True when every opening bracket has a matching closing bracket."""
    opening = {"[": "]", "(": ")", "{": "}"}
    stack: list[str] = []

    for character in text:
        if character in opening:
            stack.append(opening[character])
        elif character in ")]}":
            if not stack or stack.pop() != character:
                return False

    return not stack

if __name__ == "__main__":
    assert is_valid_parentheses("({[]})")
    assert not is_valid_parentheses("([)]")
    print(is_valid_parentheses("{python: [1, 2]}"))
