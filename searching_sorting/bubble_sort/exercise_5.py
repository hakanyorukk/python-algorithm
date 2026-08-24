def main():
    nums = [5, 1, 4, 2, 8]
    bubble_sort(nums)
    print(nums)

def bubble_sort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped=True
        if not swapped:
            break

if __name__ == "__main__":
    main()