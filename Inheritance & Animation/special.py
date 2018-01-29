'''
MY SPECIAL TELEPORTS AND KILLS BALLS. 
'''
from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2

class Special(Pulsator,Mobile_Simulton):
    global acount 
    acount = 40
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,20,20,0,5)
        self.randomize_angle()
        self.radius = 7
        
        
    def update(self,balls):
        self.move()
        for prey2 in balls:
            if isinstance(prey2, Prey):
                if self.distance(prey2.get_location()) <= 250:
                    prey2_ga = prey2.get_angle()
                    prey2_speed = prey2.get_speed()
                    
                    self.set_velocity(prey2_speed,prey2_ga)
                    
                    prey2_location = prey2.get_location()
                    self.set_location(prey2_location[0],prey2_location[1])
                                    
        return Pulsator.update(self,balls)
    
    
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius,self._x+self.radius,self._y+self.radius, fill='Yellow')
        canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",
                        text="Hello TA my SPECIAL is very very unique")