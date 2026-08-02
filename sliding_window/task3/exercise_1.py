def main():
    s = "abcabcbb"
    print(longest_non_repeating_substring(s))

def longest_non_repeating_substring(s):
    left = 0
    seen = set()
    maxLength = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        seen.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    return maxLength

if __name__ == "__main__":
    main()