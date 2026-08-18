def main():
    nums = [5,2,4,6,1,7]
    target = 12
    print(two_sum(nums,target))

def two_sum(nums, target):
    hash_map = {}
    # num, index
    # required num 2
    for num in range(len(nums)):
        required_num = target - nums[num]
        if required_num in hash_map:
            return [hash_map[required_num], num]

        hash_map[nums[num]] = num
    return []
if __name__ == "__main__":
    main()