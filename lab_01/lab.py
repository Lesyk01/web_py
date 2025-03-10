
array1 = []
array2 = []

with open('lab_01/input_1.txt', 'r') as file:
    for line in file:
   
        numbers = line.split()
        if len(numbers) == 2:
            array1.append(int(numbers[0]))
            array2.append(int(numbers[1]))
            
print(array1)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):  
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

array1 = selection_sort(array1)
array2 = selection_sort(array2)

all_list = []

for i in range(len(array1)): 
    sub = array1[i] - array2[i]
    if sub < 0:
        sub = array2[i] - array1[i]  
        
    all_list.append(sub)
total_sum = sum(all_list)


print("Висновок:",total_sum)
#1660292

