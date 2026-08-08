def main():
    nums = [1, 2, 3,4,5]
    print(isContainsDuplicate(nums))

def isContainsDuplicate(nums):
    #value, index
    numIndexes = {}
    for i in range(len(nums)):
        if nums[i] in numIndexes:
            return True
        numIndexes[nums[i]] = i
    return False

if __name__ == "__main__":
    main()