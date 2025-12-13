
numbers = [10, 20, 30]
print("Initial List:", numbers)

numbers.append(40)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.pop(2)
print("After pop:", numbers)

print("Elements using for loop:")
for n in numbers:
    print(n)

total = 0
for n in numbers:
    total += n

print("Sum of elements:", total)
