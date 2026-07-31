def main():
    nums = [1,3,4,6,8,11]
    target = 10
    print(f"Indicies: {twoSum(nums, target)}" )

def twoSum(nums, target):

    left = 0
    right = len(nums) - 1

    while left<right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]

        elif sum > target:
            right -= 1
        else:
            left += 1
    return nums

if __name__ == "__main__":
    main()