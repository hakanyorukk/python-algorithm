

# list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubledNums = [num * 2 for num in nums]
evenNums = [num for num in nums if num % 2 == 0]
square_odd_nums = [num**2 for num in nums if num % 2 == 1]
big_small_nums = ['big' if num > 5 else 'small' for num in nums]
dic_mapping = {n: n*n for n in nums}

print(doubledNums)
print(evenNums)
print(square_odd_nums)
print(big_small_nums)
print(dic_mapping)

# strings
words = ["apple", "Banana", "cherry", "date", "Elderberry"]

all_uppercased = [word.upper() for word in words]
only_longer_than5 = [word for word in words if len(word) > 5]
word_length_dict = {word:len(word) for word in words}
set_first_letters = {word[0].lower() for word in words}

print(all_uppercased)
print(only_longer_than5)
print(word_length_dict)
print(set_first_letters)
#rewrite
