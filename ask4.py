import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
score1=0
score2=0
draw=0
for i in range(100):
 for i in xarti:
    for j in color:
        xartia.append([i,j])
 random.shuffle(xartia)
 player1=[]
 sum1=0
 while sum1<16:
    sum1=0
    player1.append(xartia.pop())
    # print (player1)
    for card in player1:
        if card[0] in figures:
            sum1=sum1+10
        else:
            sum1=sum1+card[0]
    print(sum1)
 if sum1>21:
    print("P2 wins!")
    score2=score2+1
 else:
    

    print("P2 joins the game") #let me add one more player
    player2=[]
    sum2=0
    while sum2<16:
        sum2=0
        player2.append(xartia.pop())
        # print (player2)
        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
    if sum2>21:
        sum2=0
    if sum1>sum2:
        print("P1 wins!")
        score1=score1+1
    elif sum2>sum1:
        print("P2 wins!")
        score2=score2+1
    else:
        print("draw!")
        draw=draw+1
print (score1,score2,draw)


score1=0
score2=0
xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
for j in range (100):
  for i in xarti:
     for j in color:
         xartia.append([i,j])
     random.shuffle(xartia)
     player1=[]
     sum1=0
     while sum1<16:
      sum1=0
      flag1=True
      while flag1==True:
         player1.append(xartia.pop())
         if player1 in figures:
               flag1=False
         else:
            player1.append(xartia.pop())

            
      print (player1)
      for card in player1:
        if card[0] in figures:
            sum1=sum1+10
        else:
            sum1=sum1+card[0]
      print(sum1)
     if sum1>21:
      print("P2 wins!")
      score2=score2+1
     else:


      print("P2 joins the game") #let me add one more player
     player2=[]
     sum2=0
     while sum2<16:
        sum2=0
        flag=True
        while flag==True:
             player2.append(xartia.pop())
             if player2 in figures:
               player2.append(xartia.pop())
             else:
               flag=False

        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
     if sum2>21:
        sum2=0
     if sum1>sum2:
        print("P1 wins!")
        score1=score1+1
     elif sum2>sum1:
        score2=score2+1
        print("P2 wins!")
     else:
        print("draw!")
   
  print(score1,score2)

