def main():

    nums = [1, 2, 1]
    k = 2
    print(is_contains_nearby_duplicate(nums, k))

def is_contains_nearby_duplicate(nums, k):
    map = {}
    # value, index

    for i in range(len(nums)):
        if nums[i] in map and i - map[nums[i]] == k:
            return True
        map[nums[i]] = i

    return False

if __name__ == "__main__":
    main()