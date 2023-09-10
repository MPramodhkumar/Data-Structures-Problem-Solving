def SelectionSort(n,arr):
    for i in range(n):
        min_ele=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ele]:
                min_ele=j
            arr[i],arr[min_ele]=arr[min_ele],arr[i]
def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=[int(ele) for ele in input().split()]
        SelectionSort(n,arr)
        for k in range(n):
            print(arr[k], end=" ")
main()