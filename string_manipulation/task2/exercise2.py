def main():
    s = input("Enter string: ")
    print(f"Vowels counts in the {s} -> {countsVowels(s)}")

def countsVowels(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    main()
