from collections import Counter

def normalize(text):
    words = text.split()
    stripped_words = []
    for word in words:
        stripped_word = "".join(ch.lower() for ch in word if ch.isalpha())
        if stripped_word:
            stripped_words.append(stripped_word)
    return stripped_words

def word_pairs(words):
    pairs = []
    for i in range(len(words)-1):
        pairs.append((words[i], words[i+1]))
    return pairs

def top_pairs(text,n=10):
    words = normalize(text)
    return Counter(word_pairs(words)).most_common(n)

def main():
    text = open("sample.txt").read()

    print(normalize("The dog. The DOG!") == ["the", "dog", "the", "dog"])
    print(word_pairs(["a", "b", "c"]) == [("a", "b"), ("b", "c")])
    print(word_pairs(["only"]) == [])
    print(word_pairs([]) == [])
    print(len(normalize(text)) == 23)
    print(len(word_pairs(normalize(text))) == 22)
    print(top_pairs(text, 3) == [(('the', 'quick'), 3), (('quick', 'brown'), 3), (('brown', 'fox'), 3)])
    print(len(top_pairs(text, 100)) == 19)  # fewer pairs exist than requested
    print(top_pairs("", 5) == [])
    print(top_pairs("hello", 5) == [])

if __name__ == "__main__":
    main()