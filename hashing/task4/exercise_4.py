def main():
    nums = [1, 2, 1]
    k = 2
    print(is_contains_nearby_duplicate(nums, k))

def is_contains_nearby_duplicate(nums, k):
    # value, index
    numIndexes = {}
    for i in range(len(nums)):
        # if check
        if nums[i] in numIndexes and i - numIndexes[nums[i]] == k:
            return True
        # add to hashMap
        numIndexes[nums[i]] = i

    return False

if __name__ == "__main__":
    main()