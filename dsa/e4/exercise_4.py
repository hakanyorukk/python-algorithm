def main():
    a = [1,3,5]
    b = [2,4,6]
    print(merge_sorted(a,b))

def merge_sorted(a,b):
    left=0
    right=0
    merged_list=[]
    while left<len(a) and right<len(b):
        if a[left] > b[right]:
            merged_list.append(b[right])
            right+=1
        else:
            merged_list.append(a[left])
            left+=1
    while left<len(a):
        merged_list.append(a[left])
        left+=1
    while right<len(b):
        merged_list.append(b[right])
        right+=1
    return merged_list

if __name__ == "__main__":
    main()