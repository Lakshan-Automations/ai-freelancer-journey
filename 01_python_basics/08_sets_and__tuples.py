cities = ("Colombo","Melbourne","New York")
print(cities[0])

fruits = {"papaya","mango","banana","avacado","mango"}
fruits.add("grapes")
fruits.remove("papaya")

print(fruits)

numbers = {1, 1, 2, 3, 3, 4}
print(numbers)

# 1. Define the original list
nums = [1, 2, 2, 3, 4, 4, 5]

# 2. Convert list to set (removes duplicates)
unique_set = set(nums)

# 3. Convert set back to a list
cleaned_list = list(unique_set)


# 4. Print the result
print(cleaned_list)