t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(ele) for ele in input().split()]
    alone_number=arr[0]
    for i in range(1,len(arr)):
        alone_number=alone_number^arr[i]
    print(alone_number)


# arr=[int(ele) for ele in input().split()]
# for num in arr:
#     if arr.count(num)==1:
#         print(num)



# def find_single(arr):
#     frequency_map = {}
#     for num in arr:
#         if num in frequency_map:
#             frequency_map[num] += 1
#         else:
#             frequency_map[num] = 1

#     for num, frequency in frequency_map.items():
#         if frequency == 1:
#             return num
# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# print(find_single(arr))
