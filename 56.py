har=input()
a=0
b=0
for i in range(len(har)):
  if(har[i].isdigit()):
    a=a+1
  elif(har[i].isalpha()):
    b=b+1
  else:
    g=0  
if (a>=1 and b>=1):
  print("yes")  
else:
  print("no")    

