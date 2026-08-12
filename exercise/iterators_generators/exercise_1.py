def main():
    # nums = [10,20,30]
    # it = iter(nums)
    # while True:
    #     try:
    #         x = next(it)
    #     except StopIteration:
    #         break
    #     print(x)

    # for num in countdown(5):
    #     print(num)

    g = noisy()
    print(next(g))
    print(next(g))




    # import sys
    # lst = [x for x in range(100000)]
    # gen = (x for x in range(100000))
    # print(sys.getsizeof(lst), sys.getsizeof(gen))

  # total = 0
  #   for num in even_numbers(12):
  #       total += num
  #   print(total)
  #
  #   for i, n in enumerate(fib()):
  #       if i >= 10:
  #           break
  #       print(n)

def countdown(n):
    i = n
    while i >= 1:
        yield i
        i -= 1

def noisy():
    print("starting")
    yield 1
    print("between 1 and 2")
    yield 2
    print("finished")

def even_numbers(limit):
    i = 0
    while i <= limit:
        if i % 2 == 0:
            yield i
        i += 1

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
if __name__ == "__main__":
    main()