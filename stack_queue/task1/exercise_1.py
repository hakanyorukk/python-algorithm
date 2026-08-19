def main():
    s = "{[()]}"
    print(is_valid_parentheses(s))

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:          # loop through each character
        if char in pairs.values(): # if opening bracket, push to stack
            stack.append(char)
        elif char in pairs:      # if closing bracket, check the stack
            if not stack:           # if the stack is empty return false
                return False
            if stack.pop() != pairs[char]: # if isn't the matching opener for this closer
                return False               # return false
    return len(stack) == 0

if __name__ == "__main__":
    main()