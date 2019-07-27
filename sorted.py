n=int(input())
a=[]
for i in range(n):
	l=list(map(int,input().split()))
	a.extend(l)
a.sort()
print(*a)
