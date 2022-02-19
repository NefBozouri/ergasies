import random
board= [[" " for i in range (8)]for i in range (8)]
print (board)
sum1=0
sum2=0
for i in range (100):
 row=[]
 col=[]
 for i in range (3):
    row.append(random.randint(1,8))
    col.append(random.randint(1,8))
 #for player1's bishop
 T=False
 if row[0]-col[0]==row[2]-col[2] |row[0]+col[0]==row[2]+col[2]:
     print("Player 1 wins")
     sum1=sum1+2
     T=True
 #for player2's queen
 if row[2]==row[0] | col[2]==col[0] | row[0]-col[0]==row[2]-col[2] | row[0]+col[0]==row[2]+col[2]:
     print ("player2 wins")
     sum2=sum2+1
 if row[2]==row[1] | col[2]==col[1] | row[1]-col[1]==row[2]-col[2] | row[1]+col[1]==row[2]+col[2]:
    print ("player2 wins")
    sum2=sum2+1
 #for player1's tower
 if (row[1]==row[2] | col[2]==col[1]) & T==False:
     print ("Player1 wins")
     sum1=sum1+2
print ("player1 score:",sum1)
print ("player2 score:",sum2)
