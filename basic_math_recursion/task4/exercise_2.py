def main():
    while True:
        num = input("Enter num: ")
        if num == "" or num == "exit":
            print("Exiting...")
            break
        print(sum_of_digits(int(num)))

def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

if __name__ == "__main__":
    main()