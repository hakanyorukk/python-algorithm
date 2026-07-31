def main():
    nums = [1,2,1]
    k = 2
    print(isContainsNearbyDuplicate(nums,k))

def isContainsNearbyDuplicate(nums, k):
    if nums is None and k is None:
        return False
    hashMap = {}
    # key -> actual num
    # value -> index

    # num -> 0,1,2,3
    for num in range(len(nums)):
        if nums[num] in hashMap and num - hashMap[nums[num]] <= k:
            return True

        hashMap[nums[num]] = num
    return False


if __name__ == "__main__":
    main()