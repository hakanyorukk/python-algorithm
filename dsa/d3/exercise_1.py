def main():
    s = "race a car"
    print(palindrome(s))

def palindrome(s):
    clean_s = ""
    for i in range(len(s)):
        if s[i].isalpha():
           clean_s += s[i].lower()
    print(clean_s)

    left = 0
    right = len(clean_s)-1
    while left < right:
        if clean_s[left] != clean_s[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    main()