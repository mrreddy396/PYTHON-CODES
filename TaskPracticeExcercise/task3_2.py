numbers = [5, 12, 8, 25, 6, 14, 3, 18, 10, 22]
total = 0
# print the sum of even numbers
for num in numbers:
    if num % 2 == 0:
        total = num + total
print("Sum of even numbers:", total)

# print the maximum value
max_value = max(numbers)
print("Maximum value:", max_value)

# Create a new list of numbers greater than 10
i = []
for num in numbers:
    if num > 10:
        i.append(num)
print("Numbers greater than 10:", i)
