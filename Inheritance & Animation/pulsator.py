# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

from random import randint
from blackhole import Black_Hole

class Pulsator(Black_Hole):
    global acount
    acount = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.radius = randint(20, 40)/2
    
    def update(self,balls):
        aset = Black_Hole.update(self,balls)
        global acount
        
        if len(aset) == 1:
            for i in aset:
                self.radius += 1
        
        if len(aset) == 0:
            acount -= 1
            if acount < 0:
                self.radius -=1
                acount = 30
                
        if self.radius < 1:
            return self.return_finished(balls)
           
                
        return aset
    
    def return_finished(self,balls):
        finished = Black_Hole.update(self,balls)
        finished.add(self)
        return finished