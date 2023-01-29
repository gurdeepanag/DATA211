from SimpleGraphics import *
# From defines the library or python file we are bringing into this code! So in our folder/workspace, we imported SimpleGraphics and import means which functions are we deciding to bring in.
# The * next to import means to import all functions!! Otherwise, you can press Ctrl + Spacebar to see all available functions.
# Use Command + / to comment out code quickly by the way

HistogramTitle = input("Please enter the name of your histogram chart title: ")
Bar1_Value = int(input("Type in the value of the first bar: "))
Bar2_Value = int(input("Type in the value of the second bar: "))
Bar3_Value = int(input("Type in the value of the third bar: "))
Bar1_Colour = input("Type in the colour of the first bar: ")
Bar2_Colour = input("Type in the colour of the second bar: ")
Bar3_Colour = input("Type in the colour of the third bar: ")
Chart_X_Coord = int(input("Type in the x-coordinate location of the chart: "))
Chart_Y_Coord = int(input("Type in the y-coordinate location of the chart: "))

# This line of code below creates an x-axis with a length of 400 from wherever the user decides the x-coordinate
X_Axis = line(Chart_X_Coord, Chart_Y_Coord, Chart_X_Coord + 400, Chart_Y_Coord)
# This line of code below creates an y-axis with a length of 300 from wherever the user decides the y-coordinate
Y_Axis = line(Chart_X_Coord, Chart_Y_Coord, Chart_X_Coord, Chart_Y_Coord - 300)

# These next 2 lines are for centering the chart title a fixed amount above the graph, relative to the user's given x & y coordinates
setFont("Arial",35)
text(Chart_X_Coord + 200, Chart_Y_Coord - 320, HistogramTitle)

#Bar 1 details
setFill(Bar1_Colour)
rect(Chart_X_Coord + 50 , Chart_Y_Coord, 100, -Bar1_Value)

#bar2 details
setFill(Bar2_Colour)
rect(Chart_X_Coord + 150 , Chart_Y_Coord, 100, -Bar2_Value)

#bar3
setFill(Bar3_Colour)
rect(Chart_X_Coord + 250 , Chart_Y_Coord, 100, -Bar3_Value)