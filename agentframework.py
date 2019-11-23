
import random

class Agent(): # Sheep
    
    # Constructing Agent class.
    def __init__(self,environment,agents, y, x):
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
   # Calculate distance between Agents.
    def distance_between(self, agent): 
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5
    
    # Agents (Sheep) eat grass within the environment, once eaten the patch is darker and pixels are reduced.
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10   
      
    # Distance between two Agents is calculated. If Agents are sufficiently close together food is shared.
    def share_with_neighbours(self, neighbourhood):
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
        if distance <= neighbourhood:
            sum = self.store + self.agents[i].store
            average = sum/2
            self.store = average
            self.agents[i].store = average
            print ("sharing" + str(distance) + " " + str(average))                    
         
    # Returns string with x and y values, so coordinates can be traced back.              
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
      
     # Agents move.
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1) 
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
        print(self.__str__() + "Sheep Killed")
   
            
class Foxes(): # Foxes
    
    # Constructing Agent class.
    def __init__(self,environment,agents, y, x):
        self.x = random.randint(0, 100)
        self.y = random.randint(0,100)
        self.environment = environment
        self.agents = agents #foxes knowing where sheep are
        self.store = 0
   
   # Calculate distance between sheep& foxes.
    def distance_between_foxes(self, agent): 
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5     
     
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
        
     # Returns string with x and y values               
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
                
 
    
    
           
    
   
            
            
 
   
        