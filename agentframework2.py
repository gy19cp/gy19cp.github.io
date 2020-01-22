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
import random

# Constructing Agent (Drunks) class.
class Agent():
    
    def __init__(self,environment,agents, police, house_number):
        """
        Function:   Initiate class Agent (Drunks) and generate the house numbers.
                    Define xy values, the environment and a way to determine if an agent has reached home or not. 
                    The Pub and Houses are at specific, pre-defined locations, as defined in the drunkenviro.txt file. 
                    Agents begin at the pub in the centre of the environment and return to each individual agents home. 
                    The route agents take to get home is random. Agents can be guided by Police home.
                    
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.
                    environment - Raster grid from model2.py
                    agents - List of agents from model2.py
                    police - List of police from model2.py
                    house_number - Variable represents each agents individual house number from model2.py
                    at_home - Variable represents whether agents are at home, starts off as Boolean value, False.
                    
        Returns:    N/A
        """        
        self.x = random.randint(128,148) # Randomly generated.
        self.y = random.randint(138,159) # Randomly generated.
        self.environment = environment
        self.agents = agents # Drunks
        self.police = police
        self.house_number = house_number
        self.at_home = False # Agents (Drunks) are already aware they are not home when the model begins.
        
    def __str__(self):
        """
        Function:   Values are defined into a string format, so specific coordinates can be traced back if needed.
            
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate. 

        Returns:    xy coordinate values in a string.
        """
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def distance_between(self, agent): 
        """
        Function:   Calculates distance between Agents (Drunks)/ Police depending on how it is subsequently used in the code. 
            
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.
            
        Returns:    Distance between each Agents (Drunks) or Police using x y coordinates.
        """
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5

    def check_police(self):
        """
        Function:   Examines environment grid (densityenviro.txt) and shows where the nearest Police are.
            
        Parameters: closest_police - Empty to be filled with the number of Police and ordered by the closest Police to the Drunks first.
                    distance_between - Calculates the distance between Police and Agents (Drunks) and added to the closest Police list.  
        
        Returns:    Distance for the closest Police.
        """
        closest_police =[]
        
        for i in range(len(self.police)):
            distance = self.distance_between(self.police[i]) 
            closest_police.append([distance, self.police[i].x, self.police[i].y])
            closest_police.sort() # Ordered by the smallest distance first.
        
        return closest_police[0]
    
    def density(self): 
        """
        Function:   Each iteration of the Agent (Drunks) movement is tracked and a density map of agents movements is available to view as text after the model has been run. 
                    The environment starts off at 0 and as agents move '1' is added to the environment. On version 3 of this model where all work is printed in the iPython 
                    console, greater movement is shown on the density map by the environment pixels changing from blue to yellow to orange/red. On version 1, the animated 
                    agents produce a purple-white trail which shows agent movements. This can be seen in real time. 
            
        Parameters: environment - Raster grid from model2.py

        Returns:    N/A
        """
        if self.environment[self.y][self.x] >= 0: # If the environment has more than or equal to 0 units available, a value of 1 is added to be displayed in the Density Map.
            self.environment[self.y][self.x] += 1 
               
    def move(self):
        """
        Function:   Move randomly from the Pub to their respective homes or Drunks move away from the Police.
                    If the random number generated is greater than 0.5, both xy coordinates increase by 1 and the Drunk moves either North or East. 
                    If the number generated is less than 0.5, both xy coordinates decrease by 1 and the Drunk moves either South or West.
                    If the Drunks can see the Police they move away from them. 
        
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.

        Returns:    N/A
        """      
        close = self.check_police() 
        
        if close[0] <20: # If Police are within 20, they can be seen by the Drunks. 
            if self.x == close[1]: # If x values are the same, then pass as Drunks are already in a good location to be guided if neccessary.
                pass
            if self.x - close[1] < 0: # Police x value is greater than Drunks.
                self.x = self.x - 2 # Therefore, Drunks x value moves closer to 0, moving away from the Police.
            else:
                self.x = self.x + 2 # Otherwise, Drunks x value moves away from 0, moving away from the Police.
                
            if self.y == close[2]: # If y values that are the same, then pass.
                pass
            if self.y - close[2] < 0: # Police y value is greater than Drunks.
                self.y = self.x - 2 # Therefore, Drunks y value moves closer to 0, moving away from the Police.
            else:
                self.y = self.x + 2 # Otherwise, Drunks y value moves away from 0, moving away from the Police.
        
        else:  # If there are no Police within 20, Drunks move randomly as outlined in the function above. 
            if random.random() < 0.5:
                self.y = (self.y + 2) 
            else: 
                self.y = (self.y - 2) 
            if random.random() < 0.5:
                self.x = (self.x + 2) 
            else:
                self.x = (self.x - 2)     
# Boundary Effect: Agents prevented from wandering off the model edge.
            if self.y < 0:
                self.y = 0
            if self.x < 0:
                self.x = 0
            if self.y > 299:
                self.y = 299
            if self.x > 299:
                self.x = 299

    def stop(self):
        """
        Function:   Once Agents reach home, they stop moving.
            
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.

        Returns:    N/A
        """  
        self.x = self.x
        self.y = self.y # Ennsures x y locations are the same.

 
# Constructing Agent (Police) class.            
class Police(Agent): 
    
    def __init__(self,environment,agents,police, y, x):
        """
        Function:   Initiate class Police. Police can start anywhere on the town plan (drunkenviro.txt). xy values are defined. 
                    The route agents take to get home is random. 
                    
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.
                    agents - List of Police from model2.py
                                        
        Returns:    N/A
        """
        self.x = random.randint(0, 300) # Randomly generated.
        self.y = random.randint(0, 300) # Randomly generated.
        self.agents = agents    
   
    def check_drunks(self):
        """
        Function:   Examines environment grid (densityenviro.txt) and shows where the nearest Drunks are.
            
        Parameters: closest_drunks - Empty to be filled with the number of Drunks and ordered by the closest Drunks to the Police first.
                    distance_between - Calculates the distance between Agents (Drunks) and Police and added to the closest Drunks list.  
        
        Returns:    Distance for the closest Agents (Drunks).
        """
        closest_drunk = []
        
        for i in range(len(self.agents)):
            distance = self.distance_between(self.agents[i]) 
            closest_drunk.append([distance, self.agents[i].x, self.agents[i].y])
            closest_drunk.sort() # Ordered by the smallest distance first.
        
        return closest_drunk[0]
        
    def move(self):
        """
        Function:   Move randomly within the environment or Police move towards the Drunks.
                    If the random number generated is greater than 0.5, both xy coordinates increase by 1 and the Police move either North or East. 
                    If the number generated is less than 0.5, both xy coordinates decrease by 1 and the Police move either South or West.
                    If the Police can see the Drunks they move towards them and try guide them to their respective homes. 
                    
        Parameters: x - Randomly generated coordinate.
                    y - Randomly generated coordinate.

        Returns:    N/A
        """ 
        closest = self.check_drunks()
        
        if closest[0] < 30: # If Drunks are within 30, they can be seen by Police and subsequently guided if neccessary. 
            self.x += (closest[1]-self.x)/2 # Police x value halves so they become closer to the Drunks.
            self.y += (closest[1]-self.y)/2 # Police y value halves so they become closer to the Drunks.
        else:  # If Drunks are not within 30, Police move randomly.
            if random.random() < 0.5:
                self.y = (self.y + 5) 
            else: 
                self.y = (self.y - 5) 
            if random.random() < 0.5:
                self.x = (self.x + 5) 
            else:
                self.x = (self.x - 5) # Moves faster than Drunks (5 rather than 2 steps per iteration).         

# Boundary effect: Agents prevented from wandering off the model edge.   
        if self.y < 0: 
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 299:
            self.y = 299
        if self.x > 299:
            self.x = 299
 
 
   
        