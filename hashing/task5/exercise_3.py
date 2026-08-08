def main():
    s = "rat"
    t = "tra"
    print(is_anagram(s,t))

def is_anagram(s,t):
    if(len(s) != len(t)):
        return False
    count = {}
    # count -> index, count

    for i in range(len(s)):
        count[s[i]] = count.get(s[i], 0) + 1

    for j in range(len(t)):

        if t[j] not in count or count[t[j]] == 0:
            return False
        count[t[j]] = count.get(t[j], 0) - 1
    return True

if __name__ == "__main__":
    main()