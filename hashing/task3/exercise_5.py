def main():
    nums = [1, 2, 3, 1]
    print(is_contains_duplicate(nums))

def is_contains_duplicate(nums):

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    #return len(set(nums)) != len(nums)
if __name__ == "__main__":
    main()