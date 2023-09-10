def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def QuickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)

def main():
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n = int(input("Enter the number of elements: "))
        arr = [int(ele) for ele in input("Enter the elements separated by space: ").split()]
        QuickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()

if __name__ == "__main__":
    main()
