def main():

    while True:
        s = input("Enter a sentence: ")
        if s == "" or s == "exit":
            print("Exiting...")
            break
        print(f"Reversed sentence: {reverse_sentence(s)}")

def reverse_sentence(s):
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