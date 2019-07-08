n=int(input())
har=list(map(int,input().split()))[:n]
a=har.sort()
middleIndex =int( (len(har))/2)
print(har[middleIndex])