def main():
    num = input("Enter num> ")

    i = 1
    while i <= int(num):
        print(fizz_buzz(i))
        i += 1

def fizz_buzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

if __name__ == "__main__":
    main()

