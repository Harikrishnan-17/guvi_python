har,rah=map(int,input().split())
a=list(map(int,input().split()))
if har==len(a):
     for i in range(har):
          if (a[i]==rah):
            print("yes")
          else:
            print("no")  
