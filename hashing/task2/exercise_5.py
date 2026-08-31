def main():
    nums = [5,2,4,6,1,7]
    target = 12
    print(two_sum(nums,target))
    print(two_sum_pairs(nums, target))

def two_sum(nums, target):
    map = {}
    #value, index

    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in map:
            return [map[required_num], i]
        map[nums[i]] = i
    return -1

def two_sum_pairs(nums, target):
    map = {}
    pairs = set()

    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in map:
            if required_num > nums[i]:
                pairs.add((nums[i], required_num))
            else:
                pairs.add((required_num, nums[i]))
        map[nums[i]] = i
    return pairs
if __name__ == "__main__":
    main()