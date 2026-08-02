def main():

    s = input("Enter sentence: ")
    print(f"Reversed sentence: {reverseSentence(s)}")

def reverseSentence(s):
    words = s.split(" ")

    return " ".join(words[::-1])


if __name__ == "__main__":
    main()