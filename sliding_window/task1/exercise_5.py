def main():
    nums = [2,1,5,2,3,2]
    k = 3
    print(max_sum_subarray(nums, k))

def max_sum_subarray(nums,k):

    max_sum = 0
    window_sum = 0
    for i in range(k):
        window_sum+=nums[i]

    for j in range(k, len(nums)):
        window_sum = window_sum + nums[j] - nums[j-k]
        #print(window_sum, j)
        if window_sum>max_sum:
            max_sum = window_sum
    #return round(max_sum/len(nums),1)
    return max_sum

if __name__ == "__main__":
    main()