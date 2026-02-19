import turtle

s = int(input("Enter the side length (pixels): "))

pen = turtle.Turtle()
for i in range(3):
    pen.forward(s)
    pen.left(120)

turtle.done()