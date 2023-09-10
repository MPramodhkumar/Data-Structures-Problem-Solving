def bubblesort(n,arr):
  swapped=0
  for i in range(n):
    swapped=0
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        swapped+=1
    if swapped==0:
       break
def main():
  t=int(input())
  for i in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    #arr=[int(ele) for ele in input().split()]
    bubblesort(n,arr)
    for i in range(n):
       print(arr[i], end=" ")
    print()
main()