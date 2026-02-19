import turtle

side_length = int(input("Enter the side length of the hexagon (pixels): "))

pen = turtle.Turtle()
for i in range(6):
    pen.forward(side_length)
    pen.left(60)

turtle.done()