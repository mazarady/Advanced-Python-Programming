# Hunter is derived from Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    global acount 
    acount =30
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,20,20,0,5)
        self.randomize_angle()
        
        
    def update(self,balls):
        self.move()
        alist = self.return_alist(balls)

        if 0 < len(alist):
            
            self.return_diff(alist)

        return Pulsator.update(self,balls)

    def return_diff(self,alist):
        prey_diff = alist[0].get_location()
        hunter_diff = self.get_location()
            
        diff_1 = prey_diff[1]-hunter_diff[1]
        diff_2 = prey_diff[0]-hunter_diff[0]
            
        atan2_diff = atan2(diff_1,diff_2)
        self.set_angle(atan2_diff)
        
    def return_alist(self,balls):
        
        return [prey2 for prey2 in balls if isinstance(prey2, Prey) and self.distance(prey2.get_location()) <= 200]