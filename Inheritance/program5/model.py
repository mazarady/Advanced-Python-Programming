import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
balls = set()
click = None
remove_set = set()

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global cycle_count, running, balls
    cycle_count = 0
    running = False
    balls = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count, running
    if running: 
        running = False
    else:
        running = True
        update_all()
        running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global click
    click = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global balls, click, remove_set
    if str(click) == "Remove":
        try:
            for ele in balls:
                if ele.contains((x,y)):
                    remove(ele) 
        except:
            pass
    else:
        if str(click) == "Ball":
            add(Ball(x,y))
        elif str(click) == 'Black_Hole':
            add(Black_Hole(x,y))
        elif str(click) == 'Floater':
            add(Floater(x,y))
        elif str(click) == 'Hunter':
            add(Hunter(x,y))
        elif str(click) == 'Pulsator':
            add(Pulsator(x,y))
        elif str(click) == "Special":
            add(Special(x,y))
            

#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
#     
# 
# # remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    aset = {ele for ele in balls if p(ele) == True}
    return aset


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    global balls
    return_set = list()
            
    try:
            
        if running:
            cycle_count += 1
            
            for b in balls:
                if isinstance(b,Black_Hole):
                    for ele in b.update(balls):
                        return_set.append(ele)
                else:
                    b.update()
                    
        return_set = {remove(ele) for ele in return_set}
    except:
        pass

                 

#delete each simulton in the simulation from the canvas; then call display for each
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
