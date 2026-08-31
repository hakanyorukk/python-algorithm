def main():
    string = 'eceba'
    k = 2
    print(longest_k_distinct(string,k))

def longest_k_distinct(string, k):
    left=0
    max_length=0
    count={}
    best_start=0
    for right in range(len(string)):
        count[string[right]] = count.get(string[right],0)+1
        while len(count)>k:
            count[string[left]]-=1

            if count[string[left]] == 0:
                del count[string[left]]
            left+=1
        if right-left+1>max_length:
            max_length=right-left+1
            best_start=left
    return string[best_start:best_start+max_length]

if __name__ == "__main__":
    main()