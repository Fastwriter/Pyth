import turtle
t=turtle.Turtle()
t.pensize(2)
t.color('purple')
for x in range(5):
    t.fd(200)
    t.lt(60)
    t.bk(200)
def func(a, length):
    n=6
    t.lt(240)
    for i in range(n):
        t.bk(length)
        t.rt(360/n)
func(t, 200)
