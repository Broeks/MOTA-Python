# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:40:39 2015

@author: nhombroek
"""
  
   

def PlayerStatus(x):
    print(x.name," HP: %d" % x.HP)

def StartGame(i,j,k,l):
    global player1,player2
    player1=(j)
    player1.name=i
    player2=(l)
    player2.name=k    
    StartingPosition()
    PlayerStatus(player1)
    PlayerStatus(player2)
    print("----- ROUND 1: TURN 1 -----")


def StartingPosition():
    global player1,player2
    player1.x_pos=1
    player1.y_pos=1
    player2.x_pos=20
    player2.y_pos=20

def MovePos(a,x,y):
    if a.AP > (abs(x)+abs(y)):
        while a.AP>0 and abs(x)>0:
            if x>0:
                a.x_pos=a.x_pos+1
                x=x-1
                a.AP=a.AP-1
            elif x<0:
                a.x_pos=a.x_pos-1
                x=x+1
                a.AP=a.AP-1
        while a.AP>0 and abs(y)>0:
            if y>0:
                a.y_pos=a.y_pos+1
                y=y-1
                a.AP=a.AP-1
            elif y<0:
                a.y_pos=a.y_pos-1
                y=y+1
                a.AP=a.AP-1
        print(a.name,"moved to x-cord:",a.x_pos,", y-cord:",a.y_pos)
        print("Remaining AP:",a.AP)
    else:
        print("You can't move that far!")
'''
    a.x_pos=a.x_pos+x
    a.y_pos=a.y_pos+y
    a.AP=a.AP-abs(x)-abs(y)
'''
    
    

    
'''
def CheckAP(x,y):
    if x.AP < y:
        print("Not enough AP!)
    else:
'''

class TurnManager:
    Round=1
    Turn=1
    def EndTurn():
        if (TurnManager.Turn%2)==0:
            TurnManager.Round=TurnManager.Round+1
            TurnManager.Turn=1
        else:
            TurnManager.Turn=TurnManager.Turn+1
        player1.AP=20
        player2.AP=20
        print("----- ROUND:",TurnManager.Round,"TURN",TurnManager.Turn,"-----")
 


'''
Game states
before game start
player 1 turn
player 2 turn
end game
'''













"""
from bokeh.plotting import figure, gridplot, output_file, show

output_file("GameBoard.html")

x = (1,20)
y0 = (20,1)


# create a new plot
s1 = figure(width=500, plot_height=500, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)


p = gridplot([[s1]], toolbar_location=None)

# show the results
show(p)
"""

'''
print(player1.__dict__)
print(y.__name__," HP: %d" % y.HP)
'''