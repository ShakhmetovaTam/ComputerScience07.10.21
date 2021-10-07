lis = ["Андрей", "Иван", "Василий", "Петро", "Максим", "Дима"]

nums = [5, 7, 2, 4, 7, True, "Hello", 6.7, [5, 7]]

nums[0] = 50
nums[5] = 1.01

print(nums[-1][1])


# Функция списков
numbers = [5, 2, 7]
# numbers[3] = 100
numbers.append(100)
numbers.insert(1, True)

b = [5, 6, 8]
numbers.extend(b)
# numbers.reverse()
numbers.sort()

numbers.pop(-2)
numbers.remove(6)

# numbers.clear()

# print(numbers.count(True))
# print(len(numbers))

