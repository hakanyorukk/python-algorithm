def main():
    nums = [3,3]
    t = 6
    print(twoSum(nums, t))


def twoSum(nums,t):
    map = {}
    for a in range(len(nums)):
        requiredNum = t - nums[a]
        if requiredNum in map:
            return [map[requiredNum], a]

        map[nums[a]] = a
    return nums

if __name__ == "__main__":
    main()