# Check balanced parentheses
def check_balanced(s):
    if len(s) % 2 != 0:
        return False

    opening = set("{([")

    matches = {('(', ')'), ('{', '}'), ('[', ']')}

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0


s = "[](){{}}"

print(check_balanced(s))


