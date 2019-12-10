# -*- coding: utf-8 -*-
"""
@author: gy19cp

University of Leeds
___________________


Agent Framework works with both developermodel.py and usermodel.py

developermodel.py contains detailed explanatory comments, testing and debugging.
usermodel.py contains basic comments.

"""

# Libraries:
import random

# Constructing Agent (Sheep) class.
class Agent():
    
    def __init__(self,environment,agents, foxes):
        """Initiate class Agent (Sheep) and randomly generate the xy coordinates, environment and food store. All inputs from the developermodel.py and the usermodel.py"""
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.foxes = foxes
        self.store = 0 # Personal Sheep food storage, starts at 0 as Sheep haven't eaten yet.
    
    # Returns string with randomly generated xy values, so coordinates can be traced back.              
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
       
    # Calculate distance between Agents (Sheep).
    def distance_between(self, agent): 
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5 # Here x and y are randomly generated.
    
    # Agents (Sheep) eat grass within the environment, once eaten the patch is darker and pixels are reduced.
    def eat(self): 
        if self.environment[self.y][self.x] > 10: # If grass patch has greater than 10 units available, it can be eaten. Prevents overgrazing.
            self.environment[self.y][self.x] -= 10 # Eat 10 units of grass.
            self.store += 10 # 10 units of grass to Sheep food store.  
      
    # Distance between two Agents (Sheep) is calculated. If Agents are sufficiently close together food is shared.
    def share_with_neighbours(self, neighbourhood): # Neighbourhood defined in both developermodel.py and usermodel.py
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
        if distance <= neighbourhood: 
            sum = self.store + self.agents[i].store # Ensures Total Food store is calculated and food is shared equally.
            average = sum/2
            self.store = average 
            self.agents[i].store = average
            #print ("Sharing" + str(distance) + " " + str(average)) # Prints distance between Sheep that are sharing food. Print to check it is working correctly.               
               
    def move(self):
        """Agents (Sheep) move randomly, plus or minus 1 to current xy coordinates based on a random number."""
        if random.random() < 0.5:
            self.y = (self.y + 1) # If the random number generated for the sheep to move is less than 0.5, sheep move away.
        else: 
            self.y = (self.y - 1) # If the random number generated for the sheep to move is less than 0.5, sheep move closer together.
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1)     
    # Boundary Effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 100:
            self.y = 100
        if self.x > 100:
            self.x = 100
                       
    def __del__(self):
        """When Foxes are sufficiently close to Sheep, the Sheep point is removed/ 'killed' and the x y coordinates for where the Sheep was removed is printed."""
        print(self.__str__() + "Sheep Killed")


# Constructing Agent (Foxes) class.            
class Foxes(): 
    
    def __init__(self,environment,agents, foxes, y, x):
        """Initiate class Foxes and set up the xy coordinates. Environment and agents (Sheep) can continue to be used from previous code above (within the Agent Framework) and from the model."""
        if (x == None): # If no x value is found from the webpage, a random x coordinate is assigned.
            self.x = random.randint(0,100)
        else:
            self.x = x # Use x coordinate from webpage.
        if (y == None): # If no y value is found from the webpage, a random y coordinate is assigned.
            self.y = random.randint(0,100)
        else:
            self.y = y # Use y coordinate from webpage.
        self.agents = agents    
        self.store = 0 # Foxes Personal Food Store.
   
    # Calculate Distance between Sheep and Foxes.
    def distance_between_foxes(self, agent): 
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5 # Here x and y are randomly generated.     
     
    # Foxes move.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1) 
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1)         
    # Boundary effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 100:
            self.y = 100
        if self.x > 100:
            self.x = 100
            
    def eat_sheep(self,agent):
         self.agents.remove(agent)
         self.store += 1       
        
