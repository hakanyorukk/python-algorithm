def main():
          # 0, 1, 2
    nums = [1, 2, 1]
    k = 2
    print(is_contains_nearby_duplicate(nums, k))

def is_contains_nearby_duplicate(nums, k):
    if nums is None:
        return False

    hashMap = {}
    # value, index
    for i in range(len(nums)):

        if nums[i] in hashMap and i - hashMap[nums[i]] == k:
            return True

        hashMap[nums[i]] = i

    return False

if __name__ == "__main__":
    main()