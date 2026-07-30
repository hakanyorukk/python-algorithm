def main():
    nums = [1, 2, 3, 1]
    print(isContainsDuplicate(nums))

def isContainsDuplicate(nums):
    if nums is None:
        return False

    hashMap = {}
    # put in hash map key -> num,
    # value -> how money times is repeated

    for num in range(len(nums)):
        # print(nums[num])
        hashMap[nums[num]] = hashMap.get(nums[num], 0) + 1

    for index in hashMap:
        if hashMap[index] > 1:
            return True

    return False

if __name__ == "__main__":
    main()