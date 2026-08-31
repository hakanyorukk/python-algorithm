def main():
    nums = [2,1,5,2,3,2]
    k = 3
    print(max_sum_subarray(nums, k))

def max_sum_subarray(nums, k):
    max_sum = 0
    current_sum = 0
    for i in range(k):
        current_sum+=nums[i]

    for j in range(k, len(nums)):
        current_sum = current_sum + nums[j] - nums[j-k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == "__main__":
    main()