# Black_Hole is derived from Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
#         self.randomize_angle()
        
    def update(self, balls):  
        ## THIS RETURNS ALL THE BALLS THAT COME IN CONTACT WITH THE BLACK_HOLE

        return {ele for ele in balls if isinstance(ele,Prey) and self.contains(ele.get_location())}
        
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius,self._x+self.radius,self._y+self.radius, fill='Black')
        
    def contains(self,locationxy):
        return self.radius > self.distance(locationxy)
