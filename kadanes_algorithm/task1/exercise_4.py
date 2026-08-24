def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Largest sum in the array -> {max_subarray_sum(nums)}")

def max_subarray_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    temp_start=0
    best_start=0
    best_end=0

    for i in range(1, len(nums)):
        if current_sum + nums[i] > nums[i]:
            current_sum = current_sum + nums[i]
        else:
            current_sum = nums[i]
            temp_start=i

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = temp_start
            best_end = i
    #return nums[best_start:best_end+1]
    return max_sum
if __name__ == "__main__":
    main()