def main():
    s = "rat"
    t = "tar"
    print(is_anagram(s,t))

def is_anagram(s,t):

    if "".join(sorted(s)) != "".join(sorted(t)):
        return False
    return True

if __name__ == "__main__":
    main()