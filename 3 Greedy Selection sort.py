def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64,25,12,22,49]
sorted_arr = greedy_selection_sort(arr)
print("Sorted Array : ", sorted_arr)