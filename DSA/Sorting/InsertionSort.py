def InsertionSort(n,arr):
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while j>-1 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=[int(ele) for ele in input().split()]
        InsertionSort(n,arr)
        for k in range(n):
            print(arr[k], end=" ")
main()