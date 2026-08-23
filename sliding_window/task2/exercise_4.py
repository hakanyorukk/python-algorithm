def main():
    nums = [2, 1, 5, 2, 3, 2]
    k = 3
    print(average_max_subarray(nums, k))

def average_max_subarray(nums, k):

    window_sum = 0
    max_sum = 0
    for i in range(k):
        window_sum +=nums[i]
        max_sum = window_sum

    for j in range(k, len(nums)):
        window_sum = window_sum + nums[j] - nums[j-k]

        if window_sum>max_sum:
            max_sum = window_sum

    return round(max_sum/len(nums),1)

if __name__ == "__main__":
    main()