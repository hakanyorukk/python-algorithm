from collections import defaultdict


def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(algorithm(words))

def algorithm(words):
    word_dict = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        word_dict[key].append(word)

    return dict(word_dict)

if __name__ == "__main__":
    main()