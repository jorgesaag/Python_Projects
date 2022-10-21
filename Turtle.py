import turtle
window = turtle.Screen()       #Set up the window
window.colormode(255)           #Set up the color mode to be able to use rgb colors
window.bgcolor(220, 192, 139)
jorge = turtle.Turtle()   #Creates jorge
jorge.pensize(5)           #Sets pen size
jorge.color(0, 128, 128)
jorge.shape("turtle")        #Sets the shape (triangle, square, circle, turtle)
jorge.speed(1)               #Sets the speed of the drawing 1-slowest 10-fastest


dist = 5
jorge.up()                     # this "takes the pen up from the paper"
for i in range(30):    # start with size = 5 and grow by 2
    jorge.stamp()                # leave an impression on the canvas
    jorge.forward(dist)          # move jorge along
    jorge.right(24)              # and turn him
    dist = dist + 2
window.exitonclick()

