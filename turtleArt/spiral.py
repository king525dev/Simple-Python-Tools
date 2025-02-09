from turtle import *

bgcolor("black")
speed(0)
hideturtle()

for i in range(120):
     color("red")
     circle(i)
     color("orange")
     circle(i*0.8)
     right(3)
     forward(3)

for i in range(120):
     color("green")
     circle(i)
     color("lime")
     circle(i*0.8)
     left(3)
     backward(3)
     
clear()

for i in range(360):
     color("red")
     circle(i)
     color("orange")
     circle(i*0.8)
     right(3)
     forward(3)

for i in range(360):
     color("green")
     circle(i)
     color("lime")
     circle(i*0.8)
     left(3)
     backward(3)

done();