def main():
    num = int(input("Enter num> "))
    print(factorial(num))

def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num-1)

if __name__ == "__main__":
    main()