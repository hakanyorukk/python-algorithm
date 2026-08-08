def main():

    s = input("Enter sentence: ")
    print(f"Reversed sentence: {reverseSentence(s)}")

def reverseSentence(s):
    words = s.split(" ")
    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)

if __name__ == "__main__":
    main()