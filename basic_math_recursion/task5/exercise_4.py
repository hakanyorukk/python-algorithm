def main():
    num = int(input("Enter num> "))
    print(f"Reversed num: {reverse_num(num)}")

def reverse_num(num):

    result = 0
    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num = num //10
    return result

if __name__ == "__main__":
    main()