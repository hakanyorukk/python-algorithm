def main():
    a = [1,3,5]
    b = [2,4,6]
    print(merge_sorted(a,b))

def merge_sorted(a,b):

    result =[]
    left=0
    right=0

    while left<len(a) and right<len(b):
        if a[left] < b[right]:
            result.append(a[left])
            left+=1
        else:
            result.append(b[right])
            right+=1

    while left<len(a):
        result.append(a[left])
        left+=1

    while right<len(b):
        result.append(b[right])
        right+=1

    return result

if __name__ == "__main__":
    main()