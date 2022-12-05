# Import the necessary modules
import turtle
import time
import random

# Set the screen size and background color
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Set the title of the screen
screen.title("Pong")

# Define the player paddles
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Define the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.uniform(0.5, 1.5)
ball.dy = random.uniform(0.5, 1.5)

# Define the scoring system
score_left = 0
score_right = 0

# Define the pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_left}")


# Define the functions for moving the paddles
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Set the keyboard bindings
screen.listen()
screen.onkeypress(paddle_left_up, "w")
screen.onkeypress(paddle_left_down, "s")
screen.onkeypress(paddle_right_up, "Up")
screen.onkeypress(paddle_right_down, "Down")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for ball collision with paddles
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Check for ball collision with top and bottom walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Check for ball going off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write(f"Player A: {score_left}  Player B: {score_right}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write(f"Player A: {score_left}  Player B: {score_right}", align="center", font=("Courier", 24, "normal"))

    # Pause the game for a short time
    time.sleep(0.01)
