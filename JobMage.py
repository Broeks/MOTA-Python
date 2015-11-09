# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:49:18 2015

@author: nhombroek
"""

class Mage:
    HP=100
    AP=20
    Status=""
    MoveCost=1
    def FireBall(x,y):
        if x.AP < 6:
            print("Not enough AP!")
        else:
            x.AP=x.AP-5
            y.HP=y.HP-5
            print(x.name," AP: %d" % x.AP)
            print(y.name," HP: %d" % y.HP)
    def Pyroblast(x,y):
        if x.AP < 6:
            print("Not enough AP!")
        else:
            x.AP=x.AP-20
            y.HP=y.HP-40
            print(x.name," AP: %d" % x.AP)
            print(y.name," HP: %d" % y.HP)
