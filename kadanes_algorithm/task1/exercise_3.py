def main():
    nums = [-3, -1, -2]
    print(maxSubarray(nums))

def maxSubarray(nums):
    curSum = nums[0]
    maxSum = nums[0]

    for num in nums:
        curSum = max(num, curSum+num)
        maxSum = max(maxSum,curSum)
    return maxSum

if __name__ == "__main__":
    main()