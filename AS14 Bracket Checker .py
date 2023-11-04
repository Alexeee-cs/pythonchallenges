def is_balanced_brackets(input_str):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in input_str:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

test_cases = ["(a + b)", "{[x * (y + z)]}", "([)]", "((())", "())"]
for test_case in test_cases:
    if is_balanced_brackets(test_case):
        print(f"'{test_case}' has balanced brackets.")
    else:
        print(f"'{test_case}' does not have balanced brackets.")
