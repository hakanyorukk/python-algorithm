def main():
    s = "{[()]}"
    print(is_valid_parentheses(s))

def is_valid_parentheses(s):
    pairs = {")":"(", "]":"[", "}":"{"}
    seen = []

    for i in range(len(s)):
        if s[i] in pairs.values():
            seen.append(s[i])

        if s[i] in pairs:
            if not seen:
                return False
            if seen.pop() != pairs[s[i]]:
                return False
    return len(seen) == 0

if __name__ == "__main__":
    main()