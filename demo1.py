import turtle
# turtle.bgcolor("Black")
# squary = turtle.Turtle()
# squary.speed(1000)
# for i in range(200):
#     for color in ["red","blue","green"]:
#         squary.pencolor(color)
#         squary.forward(i)
#         squary.left(80)
#         squary.right(20)




turtle.color('red', 'yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()