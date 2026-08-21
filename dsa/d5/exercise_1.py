from collections import defaultdict


def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(algorithm(words))

def algorithm(words):

    anagram_words = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))

        anagram_words[key].append(word)
    return dict(anagram_words)

if __name__ == "__main__":
    main()