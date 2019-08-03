num=int(input())
har=list(map(int,input().split())) [:num]
har.sort(reverse=True)
b=0
for i in har:
  b=b*10+i
print(b)  
