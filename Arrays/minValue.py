arr = [6, 10, 2, 4, 1, 8]
minValue = arr[0]

for i in arr:
    if i < minValue:
        minValue = i

print("Lowest Value: ", minValue)