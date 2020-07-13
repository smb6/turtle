import turtle
import random
import time

t = turtle
def printer(turtle_pen_object,num,name):
    for x in range(num):
        turtle_pen_object.write(name,font =("Arial",5,"bold"))
        turtle_pen_object.left(232)
        turtle_pen_object.forward(250)


r = random.randint (90,120)
r1 = random.randint(1,8)
name1 =  input("מה השם שלך?")
user_num1 = int(input ("תבחר מספר מ 1 עד 8 - אם צדקת ניצחת "))
user_circle_or_line= int(input("תלחץ על 1 אם אתה מעדיף עיגולים ולחץ 2 אם אתה מעדיף קווים ישרים"))
chossen_circle_or_lines=0

if user_num1==r1 :
    chossen_circle_or_lines=user_circle_or_line
    print ("!!!ניצחת")
    wn =input ("איזה משפט אתה רוצה?")
else:
    if user_circle_or_line==1:
        chossen_circle_or_lines=2
    else:
        chossen_circle_or_lines=1

    print ("):הפסדתה")

print (r1)

your_name = name1
var1=["gold","silver","turquoise","red"]
var2=["green","purple","blue"]
counter=1
t.speed(1000)
for y in range(100):


    print(your_name)
    for x in range(500):

        t.forward(x)
        t.left(90)
        t.circle(x)
        printer(t, 100, wn)
        t.pencolor(var1[x % 4])
        turtle.bgcolor(var2[x % 3])
        t.width(counter)
        counter = counter + 0.001


"""""
    if chossen_circle_or_lines==1:
        t.circle(90)
        t.right(90)
        t.forward(50)

    else:

        t.forward(x+100)
    t.left(100)
time.sleep(4.5)
"""
time.sleep(10)