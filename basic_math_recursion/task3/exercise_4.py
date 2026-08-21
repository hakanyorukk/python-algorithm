def main():
    num = int(input("Enter num> "))
    print(fibonaacci(num))

def fibonaacci(num):

    if num == 0: return 0
    if num == 1: return 1
    return fibonaacci(num-1) + fibonaacci(num-2)

if __name__ == "__main__":
    main()