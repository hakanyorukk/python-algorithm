def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # → [4, -1, 2, 1]
    print(kadane_algorithm(nums))

def kadane_algorithm(nums):
    window_sum = nums[0]
    max_sum = nums[0]
    temp_start = 0
    best_start = 0
    best_end = 0
    for i in range(1, len(nums)):

        if window_sum + nums[i] > nums[i]:
            window_sum  = window_sum + nums[i]
        else:
            window_sum = nums[i]
            temp_start = i
        if window_sum > max_sum:
            max_sum = window_sum
            best_start = temp_start
            best_end = i

    return nums[best_start:best_end+1]

if __name__ == "__main__":
    main()