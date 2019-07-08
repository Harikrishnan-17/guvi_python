har=input()
s=0
for i in range(len(har)):
  if(har[i].isdigit() or har[i].isalpha() or har[i]==(" ")):
    continue
  else:
    s=s+1
print(s)