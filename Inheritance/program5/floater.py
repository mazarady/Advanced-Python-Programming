# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

from prey import Prey
import random


class Floater(Prey):
    radius = 7
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,self.radius,self.radius,0,5)
        self.randomize_angle()
    

        
    def update(self):
        
        try:
                
            if random.random() > .7:
                return_get_speed = self.get_speed()
                
                if return_get_speed -.5 > 3:
                    
                    self.return_neg_speed()
                    
                else:
                    
                    pass
                                     
                      
            else:
                return_some_speed = self.get_speed()
                if return_some_speed + .5 < 7:
                    self.return_pos_speed()
                    
                else:
                    
                    pass
     
            self.move()
            self.wall_bounce()
            
        except:
            raise AssertionError
        
    def return_neg_speed(self):
    
        return_get_speed = self.get_speed()
        return_get_angle = self.get_angle()
        self.set_speed(return_get_speed-0.5)
        self.set_angle(return_get_angle-0.5)
    
    def return_pos_speed(self):
        return_get_speed = self.get_speed()
        return_get_angle = self.get_angle()
        self.set_speed(return_get_speed+0.5)
        self.set_angle(return_get_angle+0.5)
        
    
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,self._x+Floater.radius, self._y+Floater.radius,fill="red")