def main():
    s = "abcabcbb"
    print(longest_substring(s))

def longest_substring(s):
    maxLenght=0
    seen = set()
    left = 0
    for right in range(len(s)):
        if s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        maxLenght = max(maxLenght,right-left+1)
    return maxLenght

if __name__ == "__main__":
    main()