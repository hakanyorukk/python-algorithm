def main():
    a = [3,1,4,1,5]
    b = [1,5,9,1]
    print(ordered_intersection(a,b))

def ordered_intersection(a,b):

    in_b = set(b)
    added = set()
    result = []
    for x in a:
        if x in in_b and x not in added:
            added.add(x)
            result.append(x)
    return result

if __name__ == "__main__":
    main()