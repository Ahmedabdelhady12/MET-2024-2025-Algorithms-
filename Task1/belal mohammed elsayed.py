#belal mohammed elsayed
#section 2
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Step {i + 1}: {arr}")

arr = [64, 25, 12, 22, 11]
print("Initial array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
