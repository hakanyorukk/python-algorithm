def main():
    s = input("String: ")
    print(f"Reversed string: {reverseString(s)}")


def reverseString(s):
    s = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

if __name__ == "__main__":
    main()