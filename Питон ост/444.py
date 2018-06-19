import turtle
t=turtle.Turtle()
turtle.speed(200000000)
t.color('yellow')
t.pensize(10)
def func(t, length):
    a=6
    for x in range(a):
        t.fd(length)
        t.lt(360/a)
func(t, 200)
