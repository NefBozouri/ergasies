from random import shuffle
for i in range (100):
  li=[]
  li.append(["o","0","O"])
  li.append(["o","0","O"])
  li.append(["o","0","O"])
  shuffle(li)
  for ii, sublist in enumerate(li):
    shuffle(li[ii])
  print(li)
  sum1=0
  for i in range (3):
    if (li[i][0]==li[i][1]) & (li[i][1]==li[i][2]):
        sum1=sum1+1
        break
    if (li[0][i]==li[1][i]) & (li[1][i]==li[2][i]):
        sum1=sum1+1
        break 
    if (li[i][0]>li[i][1]) & (li[i][1]>li[i][2]):
        sum1=sum1+1
        break
    if (li[0][i]>li[1][i]) & (li[1][i]>li[2][i]):
        sum1=sum1+1
        break 

 
  if (li[1][1]==li[2][2]) & (li[0][0]==li[1][1]):
      sum1=sum1+1
  if (li[2][0]==li[1][1]) & (li[1][1]==li[0][2]):
       sum1=sum1+1
  if (li[0][0]>li[1][1]) & (li[1][1]>li[2][2]):
     sum1=sum1+1
  if (li[2][0]>li[1][1]) & (li[1][1]>li[0][2]):
       sum1=sum1+1
  

print(sum1)
