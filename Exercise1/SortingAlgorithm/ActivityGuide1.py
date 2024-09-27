#1.)
#Bubble Sort
#Ascending Order
data = [23, 89, 7, 56, 44]
print("1.")
print("Arr values before Bubble Sort: ")
print(data)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print("Bubble Sort in ascending order: ")
print(data)


print()

#2.)
#Insertion Sort
#Ascending Order
print("2.")
data2 = [12,78,91,34,62]
print("Arr values before Insertion Sort: ")
print(data2)

for i in range(1, len(data2)):
    key = data2[i]
    j = i - 1

    while j>= 0 and key < data2[j]:
        data2[j + 1] = data2[j]
        j -= 1
        data2[j + 1] = key
print("Insertion Sort in ascending order: ")
print(data2)


print(

)
#3.
#Selection Sort
#Descending Order
print("3.")
data3 = [5,99,48,15,67]
print("Arr values before Selection Sort: ")
print(data3)

n = len(data3)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if data3[j] > data3[max_idx]:
            max_idx = j
    data3[i], data3[max_idx] = data3[max_idx], data3[i]
print("Selection Sort in Descending Order")
print(data3)

print()

#4.)
#Insertion Sort
#Descending Order
data4 = [38,82,35,74,13]
print("4.")
print("Arr values before Insertion Sort: ")
print(data4)

for i in range(1, len(data4)):
    for i in range(1, len(data4)):
        key = data4[i]
        j = i - 1
        while j >= 0 and key > data4[j]:
            data4[j + 1] = data4[j]
            j -= 1
            data4[j + 1] = key
print(" Insertion Sort in Descending Order: ")
print(data4)

print()

#5.
#
#
print("5.")
arr5 = [23, 44, 34, 62, 67, 48, 47, 38]
for i in range(len(arr5)):
    for j in range(0, len(arr5) - i - 1):
        if arr5[j] > arr5[j + 1]:
            arr5[j], arr5[j + 1] = arr5[j + 1], arr5[j]
print("Ascending Order: ")
print(arr5)
arr5 = [23, 34, 67, 99, 12, 91, 34, 56]
for i in range(len(arr5)):
    for j in range(0, len(arr5) - i - 1):
        if arr5[j] < arr5[j + 1]:
            arr5[j], arr5[j + 1] = arr5[j + 1], arr5[j]
print("Descending Order: ")
print(arr5)

print()

#6.
#Selection Sort
#Ascending Order
print("6.")
arr6 = [23,89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("Given Selection Sort data: ")
print(arr6)
for i in range(len(arr6)):
    min_idx = i
    for j in range(i + 1, len(arr6)):
        if arr6[min_idx] > arr6[j]:
            min_idx = j
    arr6[i], arr6[min_idx] = arr6[min_idx], arr6[i]
print("Ascending Order in Selection Sort: ")
print(arr6)

print()

#7.
# Even and Odd
#in item number 6
print("7.")
combined_dataset = arr6
combined_dataset.sort()

even_values = [x for x in combined_dataset if x % 2 == 0]
odd_values = [x for x in combined_dataset if x % 2 != 0]

print("Even values: ", even_values)
print("Odd values: ", odd_values)





