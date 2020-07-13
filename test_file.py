"""""
# angle = int(input("Enter desired angle"))
def draw_infinity(radius):
    # מצייר אינסוף
    t.circle(radius)
    t.circle(radius, 90)
    t.circle(-radius)


def draw_david_shield(radius):
    turtle.circle(radius, 360, 3)
    turtle.penup()
    # turtle.circle(radius, 180)
    turtle.setposition(x=0, y=radius*2)
    turtle.pendown()
    turtle.circle(-radius, 360, 3)

# for x in range(100, 0, -10):
#      t.circle(x)

# for x in range(10):
#     t.pencolor("gold")
#     t.forward(x)
#     t.left(98)

# t.hideturtle()
t = turtle
#draw_infinity(radius=100)
draw_david_shield(radius=50)

# turtle.color("black", "red")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.fillcolor("violet")
# turtle.end_fill()

# turtle.ht()
input("Just wait here.......")

"""
import turtle
import time

""

t = turtle
t.speed(1000000)
var1=["gold","silver","turquoise","red"]
var2=["green","purple","blue"]
counter=1


def squre(length,turtle_pen_object):
    for x in range(4):
        turtle_pen_object.forward(length)
        turtle_pen_object.left(90)

def printer(turtle_pen_object,num,name):
    for x in range(num):
        turtle_pen_object.write(name,font =("Arial",5,"bold"))
        turtle_pen_object.left(232)
        turtle_pen_object.forward(250)


your_name = "דניאל המןרה של עיליי בתכנות"

print(your_name)
for x in range (500):
    t.forward(x)
    t.left(50)
    t.circle(x)
    printer(t,100,your_name)
    t.pencolor(var1[x%4])
    turtle.bgcolor(var2[x%3])
    t.width(counter)
    counter=counter+0.001

time.sleep(15)


def boom5 (num):
    print(num*5)



