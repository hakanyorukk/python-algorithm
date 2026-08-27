from collections import Counter


def main():
    s = "rat"
    t = "tar"
    print(is_anagram_2(s,t))

def is_anagram(s,t):
    if len(s) != len(t):
        return False
    char_count = {}
    # value, count
    for i in s:
        char_count[i] = char_count.get(i, 0) + 1

    for j in t:
        if j not in char_count or char_count[j] == 0:
            return False
        char_count[j] = char_count.get(j, 0) - 1
    return True

def is_anagram_2(s,t):
    # count_s = Counter(c for c in s)
    # count_t = Counter(c for c in t)
    #
    # if count_s==count_t:
    #     return True
    # return False
    return Counter(s)==Counter(t)

if __name__ == "__main__":
    main()