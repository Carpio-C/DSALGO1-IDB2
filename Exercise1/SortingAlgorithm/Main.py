arr1 = [10,2,3,1,1,4,89,21]
#printing the arr1
#insertion sort
print("arr1")
print(arr1)
for i in range(1, len(arr1)):
    key = arr1[i]
    j = i - 1
    #move element of arr1[0..i-1]
    #that are greater than key
    #to one position ahead of their current position

    while j>= 0 and key < arr1[j]: #change the condition from ascending to descending
        arr1[j + 1] = arr1[j]
        j -= 1
        arr1[j + 1] = key

print("arr1 after insertion sort: ")
print(arr1)

#selection sort
arr2 = [10,2,3,1,1,4,89,21]
print("arr2 before selection sort: ")
print(arr2)

for i in range (len(arr2)):
    min_idx = 1
    for j in range(i + 1, len(arr2)):
        if arr2[min_idx] > arr2[j]:
            min_idx = j
            # swapping the value from our array
            arr2[i], arr2[min_idx] = arr2[min_idx], arr2[j]
print("arr2 values after selection sort")
print(arr2)

#Bubble Sort
arr3 = [10,2,3,1,1,4,89,21]
print("arr3 values before Bubble Sort: ")
print(arr3)
for i in range(len(arr3)):
    for j in range(0, len(arr3) - i - 1):
        if arr3[j] > arr3[j + 1]:
            arr3[j], arr3[j + 1], arr3[j]
print("arr3 values after Bubble sort: ")
print(arr3)

def BubbleSort(arr3):
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1]
print("arr3 values after bubble sort: ")
print(arr3)

