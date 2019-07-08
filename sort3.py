h=int(input())
a =[]
a=list(map(int,input('').split()))
a.sort()
for i in range(0,h,1):
  print(a[i],end=' ')