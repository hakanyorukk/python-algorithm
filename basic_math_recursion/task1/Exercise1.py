def main():
    num = int(input("Enter num> "))

    j = 1
    while j <= num:
        fizz_buzz(j)
        j += 1

def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 5 ==0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

if __name__ == "__main__":
    main()