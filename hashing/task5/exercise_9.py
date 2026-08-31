from collections import Counter

def main():
    s = "rat"
    t = "car"
    print(is_anagram(s,t))

def is_anagram(s,t):

    if len(s) != len(t):
        return False
    count = {}
    #value -> count

    for i in s:
        count[i] = count.get(i,0)+1

    for j in t:
        if j not in count or count[j] == 0:
            return False
        count[j] = count.get(j,0)-1
    # if "".join(sorted(s)) != "".join(sorted(t)):
    #     return False
    # if Counter(s) != Counter(t):
    #     return False
    return True

if __name__ == "__main__":
    main()