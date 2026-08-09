# 1
from collections import Counter, defaultdict

nums = [3,1,4,1,5,9,2,6,5,3,5]

most = Counter(nums).most_common(1)
#print(dict(most))

# 2
names = ["Ana", "Boris", "Chen"]
ages = [25,30,28]
print(dict(zip(names,ages)))

#3
print(f"Does nums contain any number >8: {any(num>8 for num in nums)}")
print(f"Are all numbers positive: {all(num>0 for num in nums)}")

#4
#print(f"Highest paid employee: {max(employees, key=lambda employee:employee.salary)}")

#5
s = input("Enter s: ")
print(f"Is contains duplicate: {len(s) != len(set(s))}")

#6
words = ["apple", "banana", "berry", "cherry", "avocado"]
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
print(dict(groups))









