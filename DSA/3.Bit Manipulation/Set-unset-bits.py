n,k=map(int, input().split())
#set bit
print(n | (1<<k))

#unset bit

print(n&~(1<<k))
