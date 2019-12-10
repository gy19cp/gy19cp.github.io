# -*- coding: utf-8 -*-
"""
@author: gy19cp

University of Leeds
___________________


agentframework.py works with both developermodel.py and usermodel.py

developermodel.py contains detailed explanatory comments, testing and debugging.
usermodel.py contains basic comments.

"""

# Libraries:
# For Web Coordinates-
import requests
import bs4

# For Graphical User Interface (GUI)-
import matplotlib
matplotlib.use('TkAgg')
import tkinter

# For Model-
import random
import agentframework 
import matplotlib.pyplot
import matplotlib.animation 
import csv


# Importing xy data from the web.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) # y values from the web
td_xs = soup.find_all(attrs={"class" : "x"}) # x values from the web
#print(td_ys[1]) # print to check if y imported correctly
#print(td_xs[1]) # print to check if x imported correctly

# Read in the 'in.txt' document, which opens the environment data.
f = open('in.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 
environment = [] 
for row in reader: 
    rowlist = [] 
    for value in row: 
        rowlist.append(value)  
    environment.append(rowlist) 
f.close() # Close so document does not take up much memory. Values are appended to the environment so document is not needed. 

# Animation Window Guidelines:
fig = matplotlib.pyplot.figure(figsize=(7, 7)) # Figure size set.
ax = fig.add_axes([0, 0, 1, 1]) # Figure axis set.

# Sheep (Agent) and Foxes specified.
agents = [] # List of agents
foxes = [] # List of foxes
num_of_iterations = 100
num_of_agents = 50
num_of_foxes = 5
neighbourhood = 20  # Distance sheep can sense the foxes.
foxes_neighbourhood = 10 # Distance foxes can sense the sheep. Foxes have a heightened awareness so this is less than for the sheep.


# Methods:
# Constructs the Graphical User Interface (GUI) slider.
def setup_agents():
    """The number of Sheep and Foxes in the environment are chosen from interacting with a slider."""
    global num_of_agents
    global num_of_foxes
    num_of_agents = sheepslider.get()
    num_of_foxes = foxesslider.get()
    print('Total Sheep:', num_of_agents)
    print('Total Foxes:', num_of_foxes)

# Intialise Agent (Sheep) Loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, foxes))
#print('Agents:',agents[i]) # Prints to ensure Sheep xy coordinates are being generated.

# Intialise Foxes Loop against web-derived coordinates.
for i in range(num_of_foxes):
    y = int(td_ys[i].text) # Foxes are at web-derived, specific coordinates as Foxes naturally calculate their moves when killing prey.
    x = int(td_xs[i].text)
    foxes.append(agentframework.Foxes(environment, agents, foxes, x, y))
#print('Foxes:',foxes[i]) # Prints first agent to ensure model is running correctly within webpage.


# Agents move if the above specifications work.
carry_on = True	# Animation carries on running unless told otherwise.

def distance_between(agents_row_a, agents_row_b):
     """Calculates the distance between two agents, using the pythagorus theory."""
     return ((agents_row_a.x - agents_row_b.x)**2 + (agents_row_a.y - agents_row_b.y)**2)**0.5
    
def update(frame_number):
    """The update function enables the animation so agents (sheep) can move, eat and share food with their neighbours and get killed by the foxes."""
    fig.clear()   
    global carry_on
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(len(agents)): # Sheep
        """Functions below derived from agentframework.py """ 
        agents[i].move() 
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color= "white")          

    for i in range(num_of_foxes):
        """Function below derived from agentframework.py """ 
        foxes[i].move()
        for agent in agents: 
            if foxes[i].distance_between_foxes(agent)< 5:
                foxes[i].eat_sheep(agent) 
        matplotlib.pyplot.scatter(foxes[i].x, foxes[i].y, color= "orange")        
        
        if agents[i].store > 1000: # If agent food store capacity is met, model will stop before num_of_iterations stops the model.
            carry_on = False
            print ('Agent Food Store Capacity is met.')

def gen_function(b = [0]):
    """The generate function loops the animation until num_of_iterations is met."""
    a = 0
    while (a < num_of_iterations):
        yield a	# Returns control and waits for next call.
        a = a + 1
    print('Stopping Condition met. Iteration Number:', a)    


# Run Model:
def run(): # Model run as an animation.
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# Close Model:
def close():
    root.destroy()   
    
    
# Builds Main GUI window.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Constructs a Menu.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run Model", command=run) 
model_menu.add_command(label="Close Model", command=close) 

# Add Sliders.
sheepslider = tkinter.Scale(root, bd=5, from_=50, label= "Number of Sheep:", length= 200, orient= 'horizontal', resolution= 1, to= 100)
sheepslider.pack(fill= 'x') # Optimum Sheep is 50 to see full effect of animation.
foxesslider = tkinter.Scale(root, bd=5, from_=5, label= "Number of Foxes:", length= 200, orient= 'horizontal', resolution= 1, to= 15)
foxesslider.pack(fill= 'x') # Optimum Foxes is 5 to see full effect of animation.

# Sets GUI waiting for events.
tkinter.mainloop()

