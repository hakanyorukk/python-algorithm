def main():
    s = "{[()]}"
    print(is_valid_parentheses(s))

def is_valid_parentheses(s):
    stack = []
    pairs = {")":"(", "]":"[", "}":"{"}

    for c in s:
        if c in pairs.values():
            stack.append(c)

        if c in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[c]:
                return False
    return len(stack) == 0
if __name__ == "__main__":
    main()