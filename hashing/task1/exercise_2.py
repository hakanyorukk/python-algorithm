def main():
    print("test")
    user_input = input(">Input: ")
    output = first_none_repeating(user_input)
    print(output)

def first_none_repeating(s):
    if s is None or s == "":
        return '_'
    map = {}

    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1

    for j in range(len(s)):
        if map[s[j]] == 1:
            return s[j]

    return '_'

if __name__ == "__main__":
    main()