def main():
    nums = [2, 7, 11, 15, 3, 4, 8, 1]
    target = 11

    print(two_sum(nums, target))

def two_sum(nums, target):
    # value, index
    num_map = {}
    seen = set()
    for i in range(len(nums)):
        required_num = target - nums[i]

        if required_num in num_map:
            #return [nums[i], required_num]
            seen.add((min(nums[i], required_num), max( nums[i], required_num)))
        num_map[nums[i]] = i
    #return None
    return sorted(seen)

if __name__ == "__main__":
    main()