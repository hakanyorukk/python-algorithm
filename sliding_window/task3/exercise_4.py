def main():
    s = "abcabcbb"
    print(longest_substring(s))

def longest_substring(s):
    max_length = 0
    seen = set()
    left = 0
    best_start = 0

    for right in range(len(s)):

        if s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left +1
            best_start = left
    #return max_length
    return s[best_start:max_length]

if __name__ == "__main__":
    main()