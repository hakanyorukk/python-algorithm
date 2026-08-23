def main():
    s = "xyzxy"
    print(longest_substring(s))

def longest_substring(s):

    left = 0
    seen = set()
    max_length =0
    best_start = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1

        if max_length < right - left + 1:
            max_length = right - left + 1
            best_start = left
        seen.add(s[right])
    return s[best_start:best_start+max_length]
if __name__ == "__main__":
    main()