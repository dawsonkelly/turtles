import turtle

size = float(input('size? '))

t = turtle.Turtle()
t.speed(1000)
count = 0

while count < 1000:
    count = count + 1
    t.forward(size)
    size = size*1.01
    t.left(60)