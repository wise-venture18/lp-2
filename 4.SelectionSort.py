#4.	Implement Greedy search algorithm for Selection Sort

# Sample Input :+>
# Enter number of elements: 5
# Enter elements: 22 11 23 7 69

# Selection Sort using Greedy approach with user input

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i   # assume current index is minimum

        # find smallest element in remaining array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------- User Input --------
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# sort array
sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)
