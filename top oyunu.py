# top-oyunu-python
import turtle, winsound
print("hello")
pencere = turtle.Screen()
pencere.title("PinPong")
pencere.bgcolor("black")
pencere.setup(width=800, height=600)
pencere.tracer(0)

raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape('square')
raket_a.color('white')
raket_a.penup()
raket_a.goto(-350, 0)
raket_a.shapesize(5, 1)

raket_b = turtle.Turtle()
raket_b.speed(0)
raket_b.shape('square')
raket_b.color('white')
raket_b.penup()
raket_b.goto(350, 0)
raket_b.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color('white')
yazi.penup()
yazi.goto(0, 260)
yazi.write("hello Oyuncu A:0   Oyuncu B:0", align='center', font=('Courier', 24, 'bold'))
yazi.hideturtle()
puan_a = 0
puan_b = 0
