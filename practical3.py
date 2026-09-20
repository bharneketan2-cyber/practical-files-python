number = [10, 20, 30, 40, 50]

print("First element:", number[0])
print("Last element:", number[-1])

number[2] = 35
print("Updated list:", number)

number.append(60)
number.insert(1, 15)
print("After insertion:", number)

number.remove(40)
del number[0]
print("After deletion:", number)

print("Length:", len(number))
print("Max:", max(number))
print("Min:", min(number))

number.sort()
print("Sorted list:", number)