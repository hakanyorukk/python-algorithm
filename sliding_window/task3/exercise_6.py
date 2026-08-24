

def main():
    s = "abcabcbb"
    print(longest_non_repeating_substring(s))

def longest_non_repeating_substring(s):
    seen = set()
    left=0
    max_length=0
    best_start=0
    for right in range(len(s)):
        if s[right] in seen:
            seen.remove(s[left])
            left+=1
        if right-left+1 > max_length:
            max_length = right-left+1
            best_start=left
        seen.add(s[right])

    return s[best_start:max_length]

if __name__ == "__main__":
    main()
