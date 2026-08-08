def main():
    while True:
        try:
            num = input("Enter num: ")
            if num == "" or num == "exit":
                print("Exiting...")
                break
            print(f"Reversed num: {reverse_num(int(num))}")
        except ValueError:
            print("Please enter only number.")

def reverse_num(num):
    result = 0

    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num = num // 10
    return result


if __name__ == "__main__":
    main()