def main():
    s = "race e car"
    print(palindrome(s))

def palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isdigit() or ch.isalpha())
    left = 0
    right=len(cleaned)-1

    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__": main()