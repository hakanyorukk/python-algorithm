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
    result = []
    for i in range(len(words)-1):
        result.append((words[i], words[i+1]))
    return result

def top_pairs(text, n=10):
    normalized_text = normalize(text)
    return Counter(word_pairs(normalized_text)).most_common(n)

def read_text(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"File not found {str(e)}")
        return ""
def main():
    text = read_text("sample.txt")
    print(text)

    checks = [
        ("normalize first 5", lambda: normalize(text)[:5],
         ["the", "quick", "brown", "fox", "jumps"]),
        ("word count", lambda: len(normalize(text)), 23),
        ("pairs abc", lambda: word_pairs(["a", "b", "c"]),
         [("a", "b"), ("b", "c")]),
        ("pairs one word", lambda: word_pairs(["a"]), []),
        ("pairs empty", lambda: word_pairs([]), []),
        ("total pairs", lambda: len(word_pairs(normalize(text))), 22),
        ("distinct pairs", lambda: len(top_pairs(text, 1000)), 16),
        ("top 3", lambda: top_pairs(text, 3),
         [(("the", "quick"), 3), (("quick", "brown"), 3), (("brown", "fox"), 3)]),
        ("empty text", lambda: top_pairs(""), []),
        ("single word", lambda: top_pairs("hello"), []),
        ("missing file", lambda: read_text("nope.txt"), ""),
    ]

    failed = 0
    for name, fn, want in checks:
        try:
            got = fn()
        except Exception as e:
            got = f"<{type(e).__name__}: {e}>"
        if got == want:
            print(f"PASS  {name}")
        else:
            failed += 1
            print(f"FAIL  {name}\n      got : {got}\n      want: {want}")
    print(f"\n{len(checks) - failed}/{len(checks)} passed")

if __name__ == "__main__":
    main()