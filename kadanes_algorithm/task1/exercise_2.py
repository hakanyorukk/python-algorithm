def main():
    nums = [-3, -1, -2]
    print(maxSubarray(nums))

def maxSubarray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for num in nums:
        currentSum = max(num, currentSum + num)
        maxSum = max(maxSum, currentSum)
    return maxSum

if __name__ == "__main__":
    main()