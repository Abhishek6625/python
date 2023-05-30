form turtle import*
import colorsys
speed(0)
hideturtle()
bgcolor('black')
tracer(5)
width(2)
h=0.001
for i in range(90):
    color(colorsys.hsv_to_rgb(h,1,1))
    forward(100)
    left(60)
