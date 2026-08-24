def main():
    s = "rat"
    t = "tar"
    print(is_anagram(s,t))

def is_anagram(s,t):
    hash_map = {}
    for i in range(len(s)):
        hash_map[s[i]] = hash_map.get(s[i],0)+1

    for j in range(len(t)):
        if t[j] not in hash_map or hash_map[t[j]] == 0:
            return False
        hash_map[t[j]] = hash_map.get(t[j],0)-1

    return True
if __name__ == "__main__":
    main()