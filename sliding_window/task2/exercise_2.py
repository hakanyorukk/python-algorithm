def main():
    nums = [2, 1, 5, 2, 3, 2]
    k = 3
    print(average_max_subarray(nums, k))

def average_max_subarray(nums, k):
    maxSum = 0
    windowSum = 0
    for i in range(k):
        windowSum += nums[i]
        maxSum = windowSum

    j = k
    while j < len(nums):
        windowSum = windowSum + nums[j] - nums[j-k]
        maxSum = max(maxSum, windowSum)
        j += 1

    return maxSum / len(nums)
if __name__ == "__main__":
    main()