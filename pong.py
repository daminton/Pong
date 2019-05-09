import turtle
import pygame, sys
import random
#Make sure you download pygame module
#update 5/8/19:
#	1. Different background image
#	2. Added score image
#	3. Added score sound effect
#	4. Background music 
#	5. Randomized pong speed
#	6. Randomized pong path
#	7. Changed scoreboard
#	8. Optimized wait times


wn = turtle.Screen()
wn.title("Pong")
wn.bgpic("background.png")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("lightblue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.uniform(2.5,3.5)
ball.dy = random.uniform(2.5,3.5)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("-------------  Player A: 0 | Player B: 0  -------------", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.update

#Background music
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("BGM.mp3")
pygame.mixer.music.play(-1)

# Main game loop
while True:
	try:
		wn.update()

		# Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		# Border checking
		if ball.ycor() > 290:
			ball.sety(290)
			ball.dy *= -1


		if ball.ycor() < -290:
			ball.sety(-290)
			ball.dy *= -1


		if ball.xcor() > 390:
			wn.bgpic("score.png")
			ball.goto(0,0)
			score_a += 1
			pen.clear()
			pen.write("-------------  Player A: {} | Player B: {}  -------------".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
			pygame.mixer.music.load("Bounce.mp3")
			pygame.mixer.music.play()
			pygame.event.wait()
			wn.bgpic("background.png")
			ball.dx = random.uniform(2.5,3.5)
			pygame.mixer.music.load("BGM.mp3")
			pygame.mixer.music.play(-1)

		if ball.xcor() < -390:
			wn.bgpic("score.png")
			ball.goto(0, 0)
			score_b += 1
			pen.clear()
			pen.write("-------------  Player A: {} | Player B: {}  -------------".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
			pygame.mixer.music.load("Bounce.mp3")
			pygame.mixer.music.play()
			pygame.event.wait()
			wn.bgpic("background.png")
			ball.dx = random.uniform(2.5,3.5)
			pygame.mixer.music.load("BGM.mp3")
			pygame.mixer.music.play(-1)


		# Paddle and ball collisions
		if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
			ball.setx(340)
			ball.dx *= -1


		if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
			ball.setx(-340)
			ball.dx *= -1


	except KeyboardInterrupt:
		sys.exit()
