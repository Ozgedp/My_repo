Here is a traveling salesman problem,
In this project I focused on Traveling Salesman problem, as well as Test Driven Development and creating a graph with Tkinder
to follow cities that is going to be visited.


Functions starts with "visualise" names are created to apply to extend the implementation with functionality to  
visualize road maps. To visualize the road map, it follows the way "A" in the coursework. After importing the best map    
from cities.py, it uses "TEXTUAL PRINTING" method to visualise the map  
Here is an example of the output:  
     -159 -158 -157 -156 -155 -154 -153 -152 -151  
       |    |    |    |    |    |    |    |    |  
59   - 1  - 3  -    -    -    -   -    -    -  
       |    |    |    |    |    |    |    |    |  
58   -    - 2  -    -    - 6  -   -  8 -    -  
       |    |    |    |    |    |    |    |    |  
57   -    -     -    -    - 5  - 7  -    -   -  
       |    |    |    |    |    |    |    |    |  
56   -    -    -    - 4  -    -    -   -    -  
Coordinates are ranging between 90 and -90 for latitude and -180 and 180 for logitudes.  
Printed map will only show the specific range of latitudes and longitudes to cover all the cities.  
It returns a GUI window using Tkinder module, thus user can scroll up and down in the map to see all the cities.   

