def main():
    nums = [2, 7, 11, 15, 3, 4, 8, 1]
    target = 15

    print(two_sum(nums, target))

def two_sum(nums, target):
    counts = {}
    pairs = set()
    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in counts:
            #return [ counts[required_num], i]
            if required_num>nums[i]:
                pairs.add((nums[i], required_num))
            else:
                pairs.add((required_num, nums[i]))
        counts[nums[i]] = i
    return sorted(pairs)

if __name__ == "__main__":
    main()