def main():
    s = "racecar"
    print(f"Is {s} palindrome? – {is_palindrome(s)}")

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left<right:

        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    main()