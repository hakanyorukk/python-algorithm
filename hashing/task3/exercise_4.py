from collections import Counter


def main():
    nums = [1, 2, 3, 4, 5]
    print(is_constains_duplicate(nums))

def is_constains_duplicate(nums):
    # map = {}
    # # value, count
    #
    # for i in range(len(nums)):
    #     map[nums[i]] = map.get(nums[i], 0) + 1
    #
    # for j in range(len(nums)):
    #     if map[nums[j]] > 1:
    #         return True
    ctr = Counter(nums)
    for num in nums:
        if ctr[num] > 1:
            return True
    return False

if __name__ == "__main__":
    main()