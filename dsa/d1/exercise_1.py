def main():
    nums = [2, 7, 11, 15, 3, 4, 8, 1]
    target = 11

    print(two_sum(nums, target))

def two_sum(nums, target):
    map = {}
    #num, index
    pairs=[]
    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in map:
            pairs.append((nums[i], required_num))
            #pairs[nums[i]] = required_num

        map[nums[i]] = i
    return sorted(pairs, key=lambda v: v[0])

if __name__ == "__main__":
    main()