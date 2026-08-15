def main():
    nums = [1,4,5,7,8]
    print(bubble_sort(nums))

def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped == True:
            break
    return nums

if __name__ == "__main__":
    main()