def main():
    nums = [4, 2, 9, 7, 5, 1]
    target = 5
    print(linear_search(nums, target))

def linear_search(nums,target):

    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

if __name__ == "__main__":
    main()