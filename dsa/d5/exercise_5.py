from collections import defaultdict


def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(anagram_groups(words))

def anagram_groups(words):
    result = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        result[key].append(word)
    return dict(result)

if __name__ == "__main__":
    main()