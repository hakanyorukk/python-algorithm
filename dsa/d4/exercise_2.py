def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(algorithm(nums))

def algorithm(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    temp_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(nums)):

        if current_sum + nums[i] > nums[i]:
            current_sum = current_sum + nums[i]
        else:
            current_sum = nums[i]
            temp_start = i
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = temp_start
            best_end = i

    return nums[best_start:best_end + 1]

if __name__ == "__main__":
    main()