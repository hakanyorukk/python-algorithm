def main():
    while True:
        num = input("Enter num: ")
        if num == "" or num == "exit":
            print("Exiting...")
            break
        print(factorial(int(num)))

def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num-1)

if __name__ == "__main__":
    main()