def main():
    string = 'eceba'
    k = 2
    print(longest_k_distinct(string,k))

def longest_k_distinct(s, k):
    count = {}
    left = 0
    best_start=0
    max_length=0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1

        while len(count) > k:
            count[s[left]]-=1

            if count[s[left]]==0:
                del count[s[left]]
            left+=1
        if right-left+1>max_length:
            max_length=right-left+1
            best_start=left

    return s[best_start:best_start+max_length]

if __name__ == "__main__":
    main()