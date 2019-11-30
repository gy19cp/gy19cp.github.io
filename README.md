### gy19cp.github.io
Programming for Spatial Analysts: Core Skills

## Model Summary

This animated agent-based model uses Spyder (Anaconda 3). The model code interacts with an agent framework code and an environment to produce coordinates on a 'raster' grid. The coordinates for the 'Foxes' variables are produced randomly and the 'Sheep' are plotted from an online web-derived set of data points. Both the ‘Foxes’ and ‘Sheep’ variables are defined as ‘Agents’ at distinctly defined separate times within the model. The Sheep in the model- move, 'eat' the environment, share with their nearest neighbour and a selection of the Sheep are unfortunately subsequently 'killed' by the 'Foxes' when the Foxes get sufficiently close. The code uses core Python language with an object oriented approach, continuous integration and web-scraping.

## Model Instructions 

**Step 1 -**. Open Spyder (Anaconda 3). If you have not got this downloaded, it can be installed through the Anaconda Distribution [here](https://www.anaconda.com/distribution/). My Model code works with Python 3.7. Ensure when going through the installation process that you download ‘Spyder’. 

![Spyder Screenshot](http: github.jpg "Initiating Spyder").

**Step 2 -** Download the necessary files - [User Model](http://gy19cp.github.io/model.py), [Developer Model](http://gy19cp.github.io/model.py), [Agent Framework](http://gy19cp.github.io/model.py) and [‘in’.txt](https://gy19cp.github.io/in.txt). All these files should be downloaded to the computers ‘Downloads’ folder. The User Model contains basic comments for ease for the user. The Developer Model version contains explanatory comments, testing, and debugging. 

![Spyder Screenshot](http: github.jpg "Downloads").

**Step 3 -**. Once downloaded, open Spyder and open the Agent Framework file and the selected Model (either the User/Developer version). 

**Step 4 -**. Have the ‘agentframework’ file selected within Spyder and click the green right-pointed arrow to ‘Run’ it.

![Spyder Screenshot](http: github.jpg "Agent Framework").
  
**Step 5 -**. Now select the ‘model’ file within Spyder and click ‘Run’ again. This time a box entitled ‘Model’ should pop out. Click the subheading ‘Menu’ and ‘Run Model’. 
 
 ![Spyder Screenshot](http: github.jpg "Run Model").
 
When the model is run, the orange dots represent ‘Foxes’ and the white dots represent ‘Sheep’. Where there are squares of differing darkness and no sheep around it is likely a Fox has ‘eaten’ a ‘Sheep’. This model will run until a specific number of steps (‘num_of_iterations’) has been completed. 
