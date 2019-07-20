har,rah=map(int,input().split())
a=list(map(int,input().split()))
s=0
if har==len(a):
     for i in range(har):
          if (a[i]==rah):
               s+=1
     print(s)
       
