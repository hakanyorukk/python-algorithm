def main():
    s = input("Enter string: ")
    print(f"Vowels counts in the {s} -> {countsVowels(s)}")

def countsVowels(s):
    count = sum(1 for c in s.lower() if c in "aeiou")
    return count

if __name__ == "__main__":
    main()