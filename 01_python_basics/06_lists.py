colors = ["red","blue","green"]

print(colors[1])

colors[1] = "black"

print(colors)

names = ["lakshan","sandeepa","suddi"]

names.append("kella")
names.pop(1)

for name in names:
    print(name)

list_of_5_numbers = [5,6,7,8,9]

list_of_5_numbers.pop()

for number in list_of_5_numbers:
    print(number * 2)

new_list = ["january","february","march","april","may","june"]

print(new_list[0:3])

number_list = [1,43,656,867,56,45,34]

sorted_numbers_list = sorted(number_list, reverse=True)

reversed_list = sorted_numbers_list[::-1]

print(sorted_numbers_list)
print(reversed_list)

numbers = [10, 50, 20, 5, 100]

print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers[::-1])

nums = [4, 20, 1, 99, 50]

print(max(nums))
print(min(nums))

print(len(["a", "b", "c", "d", "e"]))

tools = ["mouse","keyboard","headset","powerbank",]

tools.append("smart watch")
print(tools[0],tools[4])

