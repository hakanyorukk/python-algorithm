def main():
    print("test")
    user_input = input(">Input: ")
    output = first_none_repeating(user_input)
    print(output)


def first_none_repeating(s: str):
    if s is None or s == "":
        return '_'
    map = {}

    for c in s:
        # map.put(k,v)
        # map[k] = v;
        map[c] = map.get(c, 0) + 1

    for c in s:
        if map[c] == 1:
            return c

    return '_'

if __name__ == "__main__":
    main()