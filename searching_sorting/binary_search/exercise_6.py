def main():
    nums = [82, 22, 56, 64, 73, 12]
    ordered_nums = bubble_sort(nums)
    target = 22
    print(ordered_nums)
    print(binary_search(ordered_nums, target))

def bubble_sort(nums):

    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped == False:
            break

    return nums

def binary_search(nums, target):
    left = 0
    right = len(nums)-1

    while left<=right:
        mid = left+ (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == "__main__":
    main()