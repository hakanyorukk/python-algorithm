def main():
    s = "rat"
    t = "car"
    print(is_anagram(s,t))

def is_anagram(s,t):

    if len(s) != len(t):
        return False
    # find and put how money times repeating a value
    # key -> char
    # value -> repeating time
    hashMap = {}

    for char in range(len(s)):
        # print(s[char])
        hashMap[s[char]] = hashMap.get(s[char],0) + 1

    for char in range(len(t)):
        # t[char] not in hashMap and times repeating is 0 return false
        if t[char] not in hashMap or hashMap[t[char]] == 0:
            return False

        hashMap[t[char]] = hashMap.get(t[char], 0) - 1
    return True

if __name__ == "__main__":
    main()