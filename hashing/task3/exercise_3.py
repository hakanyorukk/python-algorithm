def main():
    nums = [1, 2, 3, 1]
    print(isContainsDuplicate(nums))

def isContainsDuplicate(nums):
    # set
    seen = set()
    for num in nums:
        if num in seen:
            return True

        seen.add(num)
    return False

if __name__ == "__main__":
    main()