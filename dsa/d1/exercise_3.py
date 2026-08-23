def main():
    nums = [2, 7, 11, 15, 3, 4, 8, 1]
    target = 11

    print(two_sum(nums, target))

def two_sum(nums, target):
    seen = set()
    pairs=set()
    for num in nums:
        required_num = target - num
        if required_num in seen:
            if required_num > num:
                pairs.add((num, required_num))
            else:
                pairs.add((required_num, num))
        seen.add(num)
    return sorted(pairs)
if __name__ == "__main__":
    main()