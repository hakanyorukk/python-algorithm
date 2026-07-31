def main():
    t = "car"
    s = "rat"
    print(isAnagram(t, s))

def isAnagram(t, s):
    if len(t) != len(s):
        return False

    hashMap = {}

    for i in range(len(t)):
        hashMap[t[i]] = hashMap.get(t[i], 0) + 1

    for i in range(len(s)):
        if s[i] not in hashMap or hashMap[s[i]] == 0 :
            return False

        hashMap[s[i]] = hashMap.get(s[i], 0) -1
    return True

if __name__ == "__main__":
    main()