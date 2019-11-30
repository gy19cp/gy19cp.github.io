# gy19cp.github.io
Programming for Spatial Analysts: Core Skills

This course has developed computer programming practical skills, particuarly with the use of Spyder (Anaconda 3) to create an agent-based model, which involves writing and structuring code, getting different code to interact and gettings code to interact with users. This  model inparticular is animated and interacts with an agent code and an environment to produce coordinates on a 'raster' grid. The plotted points (coordinates) for the 'Foxes' variables are produced randomly and the 'Agents' (Sheep) are plotted from an online web-derived set of data points. The 'Agents' in the model- move, 'eat' the environment, share with their nearest neighbour and a selection of the 'Agents' are unfortunately subsequently 'eaten' by the 'Foxes' when the 'Agents' get too close. The code uses core Python language with an object oriented approach, continous integration and web-scraping.

Step 1. Open Spyder (Anaconda 3). If you have not got this downloaded, it can be installed through the Anaconda Distribution here. https://www.anaconda.com/distribution/ . My Model code works with Python 3.7. Ensure when going through the installation process that you download ‘Spyder’. 

Step 2. Select this Repository (https://github.com/gy19cp/gy19cp.github.io) hyperlink, which should take you directly to the model repository within the Github website. This contains all files for the model.

Step 3. Select the green ‘clone or download’ button and download ‘Zip’. 

Step 4. Once downloaded, select the folder, extract all into a suitable file and open Spyder.

Step 5. Within Spyder, click on ‘File’ and ‘Open’, ensuring you locate to where you previously extracted the file. Hold the shift key and choose ‘agentframework’ and ‘model’ to ‘open’. 

Step 6. Have the ‘agentframework’ file selected within Spyder and click the green right-pointed arrow to ‘Run’ it.

Step 7. Now the model will be run. Select the ‘model’ file within Spyder and click ‘Run’ again. This time a box entitled ‘Model’ should pop out. Click the subheading ‘Menu’ and ‘Run Model’. 

When the model is run, the orange dots represent ‘Foxes’ and the white dots represent ‘Sheep’. Where there are squares of differing darkness and no sheep around it is likely a ‘fox’ has ‘eaten’ a ‘sheep’. This model will run until a specific number of steps (‘num_of_iterations’) has been completed. 
       
