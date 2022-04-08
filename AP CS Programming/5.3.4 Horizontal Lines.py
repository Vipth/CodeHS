# Write a function to draw a horizontal
# line given a y position and a length

def horizontal_line(yLocation, lineLength):
    line = Line(0, yLocation, lineLength, yLocation)
    add(line)
    
horizontal_line(100, 200)
horizontal_line(200, 100)
horizontal_line(300, 50)
