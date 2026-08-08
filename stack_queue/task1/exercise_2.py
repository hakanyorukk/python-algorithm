def main():
    s = "{[(]}"
    print(is_valid_parentheses(s))

def is_valid_parentheses(s):
    stack = []
    pairs = {')':'(', ']':'[','}':'{'}

    for char in s:
        if char in pairs.values(): #inside values opening
            stack.append(char)
        if char in pairs: # inside keys, closing bracket
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    main()