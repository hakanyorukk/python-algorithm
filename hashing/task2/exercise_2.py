def main():
    nums = [1,2,3]
    t = 5
    print(twoSum(nums, t))

def twoSum(nums, t):
    hashMap = {}
    # value, index

    for i in range(len(nums)):
        requiredNum = t - nums[i]
        if requiredNum in hashMap:
            return {i, hashMap[requiredNum]}
        hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
    return nums

if __name__ == "__main__":
    main()