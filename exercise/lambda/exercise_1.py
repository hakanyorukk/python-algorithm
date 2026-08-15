
nums = [5, 3, 8, 1, 9, 2]
words = ["banana", "Apple", "cherry", "date"]
people = [("Ana", 25), ("Boris", 30), ("Chen", 22)]

print(sorted(words, key=lambda w: w.lower()))

print(sorted(people, key=lambda a: a[1]))

print(sorted(people, key=lambda a: a[0]))

print(list(map(lambda x: x** 2, nums)))

print(list(filter(lambda x: x > 4, nums)))
print([num for num in nums if num > 4])

print(max(words, key=lambda w: len(w)))

print(sorted(people, key=lambda x: x[1], reverse = True))

#print(lambda x: len(x)> 0 and x.isdigit())


