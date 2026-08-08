def main():
    nums = [3,3]
    t = 6
    print(twoSum(nums, t))

def twoSum(nums, t):
    # value, index
    counts = {}

    for i in range(len(nums)):
        requiredNum = t - nums[i]

        if requiredNum in counts:
            return [counts[requiredNum], i]
        counts[nums[i]] = i
    return nums

if __name__ == "__main__":
    main()