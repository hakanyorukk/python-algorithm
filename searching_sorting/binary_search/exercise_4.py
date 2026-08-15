def main():
    nums = [2,5,7,13,14,16,19]
    target = 14
    print(f"Index of target: {binary_search(nums,target)}")

def binary_search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid  + 1
    return -1
if __name__ == "__main__":
    main()