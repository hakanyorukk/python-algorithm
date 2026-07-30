def main():

    nums = [1, 2, 1]
    k = 2
    print(is_contains_nearby_duplicate(nums, k))


def is_contains_nearby_duplicate(nums, k):
    if nums is None:
        return False
    hashMap = {}
    # key -> num
    # value -> num_of_duplicate

    for num in range(len(nums)):

        if nums[num] in hashMap and num - hashMap[nums[num]] <= k:
            return True
        hashMap[nums[num]] = num
    return False


if __name__ == "__main__":
    main()