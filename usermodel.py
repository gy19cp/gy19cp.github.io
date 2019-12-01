# User Model
"""
The User Model contains basic comments for ease of use. For a more structured, detailed version with explanatory comments, testing, and debugging, see the Developer Model code. 
""" 

# Libraries:
import requests
import bs4
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import operator 
import agentframework 
import matplotlib.pyplot
import matplotlib.animation 
import csv


# Importing data from the web.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"}) 
td_xs = soup.find_all(attrs={"class" : "x"}) 


# Animation Window Guidelines:
environment = [] 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Sheep (Agents) and Foxes specified.
num_of_agents = 30
num_of_iterations = 200
neighbourhood = 20
agents = []
num_of_foxes = 5
foxes_neighbourhood = 10 
foxes = []


# Methods: 
def distance_between(agents_row_a, agents_row_b):
     return ((agents_row_a.x - agents_row_b.x)**2 + (agents_row_a.y - agents_row_b.y)**2)**0.5
    
def update(frame_number):
    fig.clear()   
    global carry_on
    
    random.shuffle(agents) 
    
    for i in range(len(agents)): 
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color= "white")
        print(agents[i].x, agents[i].y)
         
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)

    for i in range(len(foxes)):
        foxes[i].move()
        for agent in agents: 
            if foxes[i].distance_between_foxes(agent)< 5:
                foxes[i].eat_sheep(agent) 
    for i in range(num_of_foxes):
        matplotlib.pyplot.scatter(foxes[i].x, foxes[i].y, color= "orange")
        
def gen_function(b = [0]):
    a = 0
    while (a < num_of_iterations):
        yield a	       
        a = a + 1
                
# Read in the 'in.txt' document.
f = open('in.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 

for row in reader: 
    rowlist = [] 
    for value in row: 
        rowlist.append(value)  
    environment.append(rowlist) 
f.close() 


# Agents move if the above specifications work.
carry_on = True	

# Intialise Sheep (Agent) Loop against web-derived coordinates.
for i in range(num_of_agents):
    y = int(td_ys[i].text) 
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

# Intialise Foxes Loop-
for i in range(num_of_foxes):
    y = random.randint(0,99) 
    x = random.randint(0,99)
    foxes.append(agentframework.Foxes(environment, agents, y, x))

# Run Model:
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
 
    
# Builds Main Graphical User Interface (GUI) window.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Constructs a Menu:
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run) 

# Sets GUI waiting for events.
tkinter.mainloop()



