def main():
    # s = "abcabcbb"  # → "abc"
    # # s = "pwwkew"  # → "wke"
    # # s = ""  # → ""
    # print(longest_substring(s))
    #
    s = "xyzxy"
    print(longest_substring(s))

def longest_substring(s):
    maxLength = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        maxLength = max(maxLength,right - left +1)
    return s[left:right+1]

if __name__ == "__main__":
    main()