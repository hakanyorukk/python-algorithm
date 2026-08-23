def main():

    nums = [1, 2, 1]
    k = 2
    print(is_contains_nearby_duplicate(nums, k))

def is_contains_nearby_duplicate(nums, k):
    #hash_map -> value, index
    hash_map = {}

    for i in range(0, len(nums)):
        if nums[i] in hash_map and i - hash_map[nums[i]] == k:
            return True
        hash_map[nums[i]] = i
    return False

if __name__ == "__main__":
    main()