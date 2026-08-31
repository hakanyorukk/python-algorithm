def main():
    string = 'eceba'
    k = 2
    print(longest_k_distinct(string,k))

def longest_k_distinct(s,k):
    left = 0
    seen = {}
    best_start = 0
    max_length=0
    for right in range(len(s)):
        # while s[right] in seen:
        #
        #     seen.remove(s[left])
        #     left+=1
        # seen.append(s[right])
        #     #print(right-left)
        seen[s[right]] = seen.get(s[right], 0) + 1
        while len(seen)>k:
            seen[s[left]] -= 1

            if seen[s[left]] == 0:
                del seen[s[left]]
            left+=1

        if right-left+1 > max_length:
            max_length = right-left+1
            best_start=left


    return s[best_start:best_start+max_length]

if __name__ == "__main__":
    main()