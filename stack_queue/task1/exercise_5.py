def main():
    s = "{[()]}"
    print(is_valid_parentheses(s))

def is_valid_parentheses(s):
    pairs={")":"(", "]":"[", "}":"{"}
    stack = []

    for i in range(len(s)):
        #opening
        if s[i] in pairs.values():
            stack.append(s[i])

        #closing
        if s[i] in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[s[i]]:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    main()