# -*- coding: utf-8 -*-
"""
@author: gy19cp
Student ID: 201376715

University of Leeds
___________________

    Assessment 2
    Version 1 
___________________

agentframework2.py file is run before the model2.py file. 

"""

# Libraries imported:
# For Graphical User Interface (GUI):
import matplotlib
matplotlib.use('TkAgg')
import tkinter

# For Model:
import agentframework2 
import matplotlib.pyplot
import matplotlib.animation 
import csv

# Agents (Drunks) and Police specified.
agents = [] # List of Agents (Drunks).
police = [] # List of Police.
densitymap=[] 
num_of_iterations = 1000000
num_of_agents = 25 # Agent numbers are limited by having 25 homes.
num_of_police = 5
neighbourhood = 10  # Distance Drunks can notice the Police.
police_neighbourhood = 30 # Distance Police can notice the Drunks. 
reached_home = 0 # Number of Drunks that have reached home, starts at 0 as all Drunks start at the Pub in the centre.

# Animation Window Guidelines:
fig = matplotlib.pyplot.figure(figsize=(7, 7)) # Figure size set.
ax = fig.add_axes([0, 0, 1, 1]) # Figure axis set.

# Read in 'drunkenviro.txt' document, which opens the environment data.
f = open('drunkenviro.txt', newline='')
reader = csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) 

environment = [] 
# Arrange the Environment csv file into rows.
for row in reader: 
    rowlist = [] 
    for value in row: 
        rowlist.append(value)  
        #print(len(rowlist)) # Print to ensure rows are being created.
    environment.append(rowlist) 
f.close() # Close document to ensure efficient memory usage. Values are appended to the environment so document is not needed. 
#print(type(environment), len(environment)) # Print to ensure environment is working after being arranged into rows.

# Creating the size of the environment.
height=len(environment)
width=len(environment[0])

# Adding zeros to the Density Map environment.
for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    densitymap.append(rowlist)
#print(height,width) # Checks that the Density Map has been made.

# Pub Location within the Environment.   
for y, row in enumerate (environment):
    for x, value in enumerate (row):
        if value==1:
            xpub=x
            ypub=y
print('Pub Located') 


# Methods:
# Constructs the GUI slider.
def setup_agents():
    """
    Function:   Sets up Police in the environment by choosing a number from the GUI slider.
                Initialises Drunks and Police loops derived from agentframework2.py. Within the Drunk loop
                house number and agent location can be determined. 
                
    Parameters: num_of_police - Global variable defines number of Police as selected using the slider. 
                num_of_agents - Variable defines number of Drunks.
                environment - 300 x 300 raster grid containing the town plan.
                agents - List of Drunks.
                police - List of Police.
                x - Randomly generated coordinate. 
                y - Randomly generated coordinate.
                
    Returns:    Prints number of Drunks and Police that are going to be in the model.
                Specific Agent (Drunks) number and Boolean values, 'True' or 'False' is printed in the iPython console to show if an agent is home or not. 

    """
    global num_of_police 
    num_of_police = policeslider.get() 
    print('Total Drunks:', num_of_agents) # Prints total number of Drunks. This should always be 25.
    print('Total Police:', num_of_police) # Prints total number of Police as selected.
     
    # Initialise Agents (Drunks) Loop. 
    for i in range(num_of_agents):
        house_number = (i+1)*10
        #print("House Number:", house_number)
        agents.append(agentframework2.Agent(environment, agents, police, house_number))
        agent_location = agents[i] #  xy location of each agent is retained.
        #print("Drunks Location:",agents[i]) # Prints to ensure the Drunks xy coordinates are being generated. 

    # Initialise Police Loop.
    for i in range(num_of_police):
        police.append(agentframework2.Police(environment, agents, police, x, y))
        #print("Police:",police[i]) # Prints to ensure Police xy coordinates are being generated.

    # Movement of Agents (Drunks). 
    for i in range(num_of_agents): # Each agent is numbered, corresponding with their house.
            if agent_location.house_number==agents[i].environment[agents[i].y][agents[i].x]:
                #print("House Number:",house_number) 
                agent_location.at_home==True 
                reached_home = reached_home + 1 # When Drunks get home they are added to the count. Ensures all get home.
                agents[i].stop() # Once Drunk reaches home, they should stop moving about.  
                #print("Agent should stop at home.") 
                #print("Testing Environment-Agent value:",environment[agents[i].y][agents[i].x])
            else: 
                agent_location.at_home==False
                agents[i].move() # If Agents that have not reached home, keep moving.
                agents[i].density() # Agents continuing to move, continue adding 1 to the Density Map with each iteration.
                #print("House_Number:",house_number) # Testing to see if House Number stays the same.
                #print("Agent moves:", agents[i]) # Testing to see if the Drunk continues to move as it has not reached home yet.

            # Produces the Density Map.      
            matplotlib.pyplot.imshow(densitymap)

    for i in range(len(agents)): 
        print('agent {0}: {1}'.format(i, agents[i].at_home)) # If an agent gets home, the agent number plus 'True' is printed. 
        # Likewise if an agent does not get home, the agent number plus 'False' is printed.   
                  
# Drunks move if the above specifications work.
carry_on = True	# A Boolean value; the animation carries on running unless told otherwise.

  
def update(frame_number):
    """
    Function:   Plots the environment and enables the actions for the animation. The actions are derived from the agentframework2.py. 
                Agents (Drunks) can check an area for Police presence, move, stop moving and track movement creating a Density Map. Police 
                can check an area for presence of Drunks, move and move (heard) Drunks to suitable areas. The number of Drunks that get home
                is displayed in the model text box that runs in real time above the model. 
                Agents (Drunks) can move.
    
    Parameters: frame_number - Number of Iterations.
                carry_on - Global variable associated with Boolean values. If the Police and Drunks specifications above work, the model carries on.
                environment - 300 x 300 raster grid containing the town plan.
                num_of_agents - List of Drunks. 
                num_of_police - List of Police.
                at_home - Global variable ensures number of Drunks reaching home is able to be viewed and updated as the model progresses. 
                
    Returns:    N/A

    """
    fig.clear()   
    global carry_on 
    global at_home 
    matplotlib.pyplot.xlim(0, 300) # Determines x coordinates for the environment grid.
    matplotlib.pyplot.ylim(0, 300) # Determines y coordinates for the environment grid.
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.text(105, 310, "Drunks Home: " +str(reached_home), bbox=dict(facecolor='white', alpha=1), fontsize = 15)

    for i in range(num_of_agents): # Drunks
        """Functions below derived from agentframework2.py """ 
        agents[i].check_police()
        agents[i].move() 
        agents[i].stop()
        agents[i].density()

    for i in range(num_of_agents):
        if agents[i].at_home == True:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='green') # Drunks that get home turn green.
        else:
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='red') # Drunks that do not get home remain red.

    for i in range(num_of_police):
        """Function below derived from agentframework2.py """ 
        police[i].check_drunks()
        police[i].move()
        matplotlib.pyplot.scatter(police[i].x, police[i].y, color= "black")        

def gen_function(b = [0]):
    """
    Function:   Loops the animation until all 25 Drunks get home or Number of Iterations is met.
                Once one of these conditions has been met the model stops. 
    
    Parameters: num_of_iterations - Total iterations defined at the start of the model2.py code.
                carry_on - Produces Boolean values. If the Police and Drunks specifications above work or number of iterations are not met, the model carries on.

    Returns:    Prints iteration number. 

    """
    a = 0
    while (a < num_of_iterations) & (carry_on): 
        yield a	# Returns control and waits for next call.
        a = a + 1
    print('Stopping Condition met. Iteration Number:', a)  

def run(): 
    """
    Function:   Model run as an animation.
    
    Parameters: N/A

    Returns:    N/A    

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def create():
    """
    Function:   Enables an Excel comma-separated values (csv) document to be opened and values to be inputted 
                with the agent movements. A button can be pressed to save the movements at that particular point. 
                This forms the Density Map text file. Values change from 0 to a number depending on the movements.
    
    Parameters: environment - 300 x 300 raster grid containing the town plan.

    Returns:    N/A         

    """
    f2= open ('densitymap.csv', 'w', newline= '') # Writes the new Density Map to a csv file.
    writer = csv.writer (f2, delimiter = ',')
    for row in densitymap:
        writer.writerow(row)
    f2.close()


def close():
    """
    Function:   Model able to be closed manually before all Drunks reach home or number of iterations met.
    
    Parameters: N/A

    Returns:    N/A     

    """
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
policeslider = tkinter.Scale(root, bd=5, from_=1, label= "Step A: Choose the Number of Police.", length= 200, orient= 'horizontal', resolution= 1, to= 5)
policeslider.pack(fill= 'x') # Optimum Police is 5 to see full effect of animation.

# Adds Buttons to GUI.
button1=tkinter.Button(root, command=setup_agents, text= "Step B: Set up Drunks (25) and Police.")
button1.pack(fill='x')
button2=tkinter.Button(root, command=run, text="Step C: Run Model.")
button2.pack(fill='x')
button3=tkinter.Button(root, command=create, text="Step D: Create Density Map.")
button3.pack(fill='x')
button4=tkinter.Button(root, command=close, text="Step E: Close the Model.")
button4.pack(fill='x')

# Sets GUI waiting for events.
tkinter.mainloop()
