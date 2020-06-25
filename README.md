# Traveling Salesman

- There is a salesman who has to visit a list of cities only once and then had to finish the journey where it starts. The salesman had to minimize total distance, thus what is the best route that the salesman should follow? 

- This project is to solve classic travelling salesman problem. The code outputs an interactive Python GUI map with Tkinder to show the coordinates of the best route.

Here is the part of the interactive output map with Tkinder:

![Figure 0, Output](https://github.com/Ozgedp/Project-1/blob/master/images/gui_tkinder_3.jpg)  


## Purposes of this project

- Solving complex problems with Python 3 programming language.
- Implementing Python GUI (Graphical User Interface) programming with Tkinder package
- Writing tests (used  pytest) and *Test-Driven-Development* (TDD).
- Considering different search algorithms and data structures.


## Details of the Problem

Suppose that there are a number of "cities", as in shown in Figure 1:

![Figure 1, Cities](https://github.com/Ozgedp/Project-1/blob/master/images/cities.jpg)  

The distance between cities are calculted with euclidean distance formula.
Which  means, I assumed that the world is flat.

After visiting every city in the list exactly once, 
the salesman have to come back to city where it starts at the end of the journey.
This courney can be shown as a circuit in Figure 2.

![Figure 2. A circuit](https://github.com/Ozgedp/Project-1/blob/master/images/linked_cities.jpg)


## Data representation

I used **city-data.txt** as dataset, it has capital cities of the USA along with its latitudes, longitudes and the state information.

As an example, the first two line of the txt data looks like this,

"Alabama	Montgomery	32.361538	-86.279118  
Alaska	Juneau	58.301935	-134.41974"

## Approach to solve the problem

- In this project I used Test Driven Development approach, thus first wrote a stab for the functions in **cities.py** that does nothing and returns pass, and then I started writing the test functions by using pytest. These test functions are in **test_cities.py** file to test the possible outputs of the testable functions. 

- Then I completed writing the functions in **cities.py**. My approach to solve this problem is, I swapped cities (swapped two cities location in the list) and/or shifted the cities (changed the position of a city in the existing list). I used swap and shift combinations 10000 times to find the best cycle.

- The functions in **cities.py** that starts with "visualise" function names are created to apply to extend the implementation with functionality to visualize road maps. 

## Outputs

When you run the **cities.py** it will output two information. First it will printed the best cycle representation with the connectons city to city, and also the cost of the traveling between these cities.
Here is an example of the first output:

        Connection 1 :  Lincoln ========> Pierre     (COST: 5.1052153729977965 )  
        Connection 2 :  Pierre ========> Bismarck     (COST: 4.467358777622971 )  
        Connection 3 :  Bismarck ========> Helana     (COST: 11.46453602088514 )  
        .....  
        Connection 50 :  Des Moines =======> Lincoln     (COST: 3.152762894427983 )  

        TOTAL COST FOR THE BEST CYCLE IS 343.4879426527414 
 

The second output will print the map, its coordinates are ranging between 90 and -90 for latitude and -180 and 180 for logitudes. In the output below, columns and rows show coordinates.  The symbols "|" and "-" are printed to draw the grid of the map and the numbers betwen these symbols (1,2,3...) show the georgraphical positions of the cities. In the output below, place 1 in the position (59, -159) corresponds to the first city visited, 2 of the second, etc. 

           -159 -158 -157 -156 -155 -154 -153 -152 -151
             |    |    |    |    |    |    |    |    |
      59   - 1  - 3  -    -    -    -   -     -    -
             |    |    |    |    |    |    |    |    |
      58   -    - 2  -    -    - 6  -   -  8  -    -
             |    |    |    |    |    |    |    |    |
      57   -    -    -    -    - 5  - 7 -     -    -
             |    |    |    |    |    |    |    |    |
      56   -    -    -    - 4  -    -   -     -    -      

Printed map will only show the specific range of latitudes and longitudes to cover all the cities. Possibly the output map will not have longitudes range between -180 to +180, and latitides range between -90 to +90. Because this program will adapt the input coordinates, and will only start from input coordinates.

To show the printed map, the program returns a GUI window using Tkinder module, thus user can interactively scroll up and down in the map to see all the cities. Here is the example image of the output:

![Figure 3. Tkinder Map Representation2](https://github.com/Ozgedp/Project-1/blob/master/images/tkinder_map_2.jpg)



