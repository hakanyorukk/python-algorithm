def main():
    s = "xyzxy"
    print(longest_substring(s))

def longest_substring(s):

    left = 0
    seen = set()
    best_start = 0
    max_length = 0
    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])

        if right-left+1 > max_length:
            max_length = right-left+1
            best_start=left
    return s[best_start:best_start+max_length]

if __name__ == "__main__":
    main()