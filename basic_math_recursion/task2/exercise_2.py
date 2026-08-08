def main():
    while True:
        num = input("Enter num: ")
        if num == "" or num == "exit":
            print("Exiting...")
            break
        print(factorial(int(num)))

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
# faster iterative approach
# def factorial(num):
#     product = 1
#     for i in range(1, num+1):
#         product *= i
#     return product

if __name__ == "__main__":
    main()