# -*- coding: utf-8 -*-
"""
@author: gy19cp
Student ID: 201376715

University of Leeds
___________________

    Assessment 1
___________________

agentframework.py file is run before the model.py file. 

"""

# Libraries imported:
# For Web Coordinates-
import requests
import bs4

# For Graphical User Interface (GUI)-
import matplotlib
matplotlib.use('TkAgg')
import tkinter

# For Model-
import agentframework 
import matplotlib.pyplot
import matplotlib.animation 
import csv


# Import xy data from the html file.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) # y values from the html file.
td_xs = soup.find_all(attrs={"class" : "x"}) # x values from the html file.
#print(td_ys[1]) # Print to check if y imported correctly.
#print(td_xs[1]) # Print to check if x imported correctly.

# Read in the 'in.txt' document, which opens the environment data.
f = open('in.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 
environment = [] 

# Arrange the Environment csv file into rows.
for row in reader: 
    rowlist = [] 
    for value in row: 
        rowlist.append(value)  
    environment.append(rowlist)
    #print(type(environment), len(environment)) # Print to ensure environment is working. 
f.close() # Close document to ensure efficient memory usage. Values are appended to the environment so document is not needed. 

# Animation Window Guidelines:
fig = matplotlib.pyplot.figure(figsize=(7, 7)) # Figure size set.
ax = fig.add_axes([0, 0, 1, 1]) # Figure axis set.

# Agents (Sheep) and Foxes specified.
agents = [] # List of Agents (Sheep).
foxes = [] # List of Foxes.
num_of_iterations = 100
num_of_agents = 100
num_of_foxes = 10
neighbourhood = 10  # Distance Sheep can sense the Foxes.
foxes_neighbourhood = 20 # Foxes sense Sheep a greater distance away as Foxes have a stronger predatory instinct than Sheep.
sheepkilled = 0 # Number of Sheep killed by Foxes starts at 0.


# Methods:
# Constructs the GUI slider.
def setup_agents():
    """The number of Sheep and Foxes in the environment are chosen by operating the slider."""
    global num_of_agents # Global variable defines number of Sheep as selected using the slider.
    global num_of_foxes # Global variable defines number of Foxes as selected using the slider. 
    num_of_agents = sheepslider.get()
    num_of_foxes = foxesslider.get()
    print('Total Sheep chosen:', num_of_agents) # Prints total number of Sheep as selected.
    print('Total Foxes chosen:', num_of_foxes) # Prints total number of Foxes as selected.

# Initialise Agent (Sheep) Loop.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, foxes))
#print('Agents:',agents[i]) # Prints to ensure Sheep xy coordinates are being generated.

# Initialise Foxes Loop against html-derived coordinates.
for i in range(num_of_foxes):
    y = int(td_ys[i].text) # Foxes move according to the xy coordinates from the html file.
    x = int(td_xs[i].text)
    foxes.append(agentframework.Foxes(environment, agents, foxes, x, y))
#print('Foxes:',foxes[i]) # Prints to ensure Foxes xy coordinates are being generated.


# Agents (Sheep) move if the above specifications work.
carry_on = True	# A Boolean value; the animation carries on running unless told otherwise.

def distance_between(agents_row_a, agents_row_b):
    """Calculates the distance between two Agents (Sheep), using the pythagorus theory."""
    return ((agents_row_a.x - agents_row_b.x)**2 + (agents_row_a.y - agents_row_b.y)**2)**0.5
    
def update(frame_number):
    """The update function plots the environment and enables the actions for the animation. The actions are derived from the agentframework.py. 
        Agents (Sheep) can move, eat and share food with their neighbours and get killed by the Foxes. Foxes move and eat the Sheep. 
        The number of Sheep killed is displayed in the model text box that runs in real time above the model."""
    fig.clear()   
    global carry_on # Global variable ensures if the Foxes and Sheep specifications above work the model carries on.
    global sheepkilled # Global variable ensures number of Sheep killed is able to be viewed and updates as the model progresses. 
    matplotlib.pyplot.xlim(0, 100) # Determines the x coordinates for the environment grid.
    matplotlib.pyplot.ylim(0, 100) # Determines the y coordinates for the environment grid.
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.text(35, 105, "Sheep Killed: " +str(sheepkilled), bbox=dict(facecolor='white', alpha=1), fontsize = 15)
    
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
                foxes[i].eat_sheep(agent) # When Foxes are sufficiently close to Sheep, the Sheep is removed/'killed'.
                sheepkilled = sheepkilled + 1 # When Sheep are killed, the 'sheepkilled' text box increases by the number killed.
        matplotlib.pyplot.scatter(foxes[i].x, foxes[i].y, color= "orange")        
        
        if agents[i].store > 1000: # If Agent (Foxes) food store capacity is met, the model will stop before num_of_iterations stops the model.
            carry_on = False # A Boolean value; the animation stops once the condition (Food Store Capacity) is met.
            print ('Foxes Food Store Capacity is met.')

def gen_function(b = [0]):
    """The generate function loops the animation until num_of_iterations or Foxes Food Store Capacity is met."""
    a = 0
    while (a < num_of_iterations) & (carry_on): # Iterations/Food Store Capacity to met defined at the start of the model.
        yield a	# Returns control and waits for next call.
        a = a + 1
    print('Stopping Condition met. Iteration Number:', a)    


# Run Model:
"""Model run as an animation."""
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# Close Model:
"""Model able to be closed manually before Foxes Food Capacity or number of iterations met."""
def close():
    root.destroy()   
    
    
# Builds Main GUI window.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

# Constructs a Menu.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run Model", command=run) 
model_menu.add_command(label="Close Model", command=close) 

# Adds Sliders to GUI.
sheepslider = tkinter.Scale(root, bd=5, from_=50, label= "Step A: Choose the Number of Sheep.", length= 200, orient= 'horizontal', resolution= 1, to= 100)
sheepslider.pack(fill= 'x') # Optimum Sheep is 75 to see full effect of animation.
foxesslider = tkinter.Scale(root, bd=5, from_=5, label= "Step B: Choose the Number of Foxes.", length= 200, orient= 'horizontal', resolution= 1, to= 15)
foxesslider.pack(fill= 'x') # Optimum Foxes is 10 to see full effect of animation.

num_of_agents = sheepslider.get()
num_of_foxes = foxesslider.get()

# Adds Buttons to GUI.
button1=tkinter.Button(root, command=setup_agents, text= "Step C: Click to set up the chosen Sheep and Foxes.")
button1.pack(fill='x')
button2=tkinter.Button(root, command=run, text="Step D: Run Model.")
button2.pack(fill='x')
button3=tkinter.Button(root, command=close, text="Step E: Close the Model.")
button3.pack(fill='x')

# Sets GUI waiting for events.
tkinter.mainloop()



