def main():
    nums = [-3,-1,-2]
    print(f"Largest sum in the array -> {maxSubArraySum(nums)}")

def maxSubArraySum(nums):

    maxSum = nums[0]
    currentSum = nums[0]

    j = 1
    while j < len(nums):

        currentSum = max(nums[j], currentSum + nums[j])
        maxSum = max(maxSum, currentSum)
        j+=1
    return maxSum

if __name__ == "__main__":
    main()