har = int(input())
sa = list(map(int,input().split()))
sa.sort()
for i in range(har):
  print(sa[i],end=" ")