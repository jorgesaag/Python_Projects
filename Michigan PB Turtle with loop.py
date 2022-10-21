import turtle
window = turtle.Screen()       #Set up the window
window.colormode(255)           #Set up the color mode to be able to use rgb colors
window.bgcolor(0, 0, 0)
jorge = turtle.Turtle()   #Creates jorge
jorge.shape("arrow")        #Sets the shape (triangle, square, circle, turtle)
jorge.speed(1)               #Sets the speed of the drawing 1-slowest 10-fastest
dist = 5

for acolor in ((0, 128, 128), (37, 167, 0), (8, 76, 247), (97, 176, 176)):    # change colors
    jorge.color(acolor)
    jorge.forward(100)          # move jorge along
    jorge.left(90)              # and turn him
window.exitonclick()
