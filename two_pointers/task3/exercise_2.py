def main():
    nums = [1,2,3]
    t = 5
    print(twoSum(nums, t))

def twoSum(nums, t):

    left = 0
    right = len(nums) - 1

    while left<right:
        sum = nums[left] + nums[right]

        if sum == t:
            return {left, right}
        elif sum > t:
            right -= 1
        else:
            left +=1
    return nums

if __name__ == "__main__":
    main()