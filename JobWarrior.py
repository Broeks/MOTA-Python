# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:48:58 2015

@author: nhombroek
"""

class Warrior:
    HP=100
    AP=20
    Berzerk=0
    Status=""
    MoveCost=1
    def AxeSwing(x,y,z):
        z = Warrior.Berzerk
        if x.AP < 6:
            print("Not enough AP!")
        elif (x.x_pos-y.x_pos!=0 and abs(x.y_pos-y.y_pos)!=1) or (x.y_pos-y.y_pos!=0 and abs(x.x_pos-y.x_pos)!=1):
            print("Target out of range!")
        else:
            if z == 0:
                x.AP=x.AP-6
                y.HP=y.HP-6
                print(x.name," AP: %d" % x.AP)
                print(y.name," HP: %d" % y.HP)
            else:
                x.AP=x.AP-6
                y.HP=y.HP-12
                x.HP=x.HP-3
                print(x.name," AP: %d" % x.AP)
                print(y.name," HP: %d" % y.HP)
    def AxeThrow(x,y):
        if x.AP < 6:
            print("Not enough AP!")
        else:
            x.AP=x.AP-6
            y.HP=y.HP-6
            print(x.name," AP: %d" % x.AP)
            print(y.name," HP: %d" % y.HP)