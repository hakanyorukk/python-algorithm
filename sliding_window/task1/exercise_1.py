def main():
    nums = [2,1,5,2,3,2]
    k = 3
    print(max_sum_subarray(nums, k))

def max_sum_subarray(nums, k):
    maxSum = 0
    windowSum = 0

    for i in range(k):
        windowSum += nums[i]
        maxSum = windowSum

    j = k
    while j < len(nums) - 1:
        windowSum = windowSum + nums[j] - nums[j-k]
        maxSum = max(windowSum, maxSum)
        j += 1

    return maxSum

if __name__ == "__main__":
    main()