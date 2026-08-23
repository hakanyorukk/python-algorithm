from collections import defaultdict

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(algorithm(words))

def algorithm(words):
    word_list = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))

        word_list[key].append(word)

    return dict(word_list)

if __name__ == "__main__":
    main()