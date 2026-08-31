def main():
    s = "rat"
    t = "tar"
    print(is_anagram(s,t))

def is_anagram(s,t):
    count = {}
    if len(s) != len(t):
        return False

    for i in s:
        count[i]=count.get(i,0)+1
    for j in t:
        if j not in count or count[j] == 0:
            return False
    return True

if __name__ == "__main__":
    main()