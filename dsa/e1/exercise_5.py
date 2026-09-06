def main():
    string = 'eceba'
    k = 2
    print(longest_k_distinct(string,k))

def longest_k_distinct(string, k):

    left=0
    right=0
    count ={}
    for right in range(len(string)):
        count[string[right]] = count.get(string[right], 0) + 1
        while len(count) > k:
            count[right]-=1