arr = [6, 10, 2, 4, 1, 8]
maxValue = arr[0]

for i in arr:
    if i > maxValue:
        maxValue = i

print("Higest Value: ", maxValue)