import turtle
import os
import math
import random

# Render sceen
sc = turtle.Screen()
sc.bgcolor("black")
sc.title("Space Invaders")
# sc.bgpic("space_invaders_background.jpg")

# display shapes
# turtle.register_shape("invader.gif")
# turtle.register_shape("player")

# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left")
score_pen.hideturtle()

# create player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# create number of enemies
number_of_enemies = 10
enemies = []
enemy = turtle.Turtle()
# add enemies
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# question this
enemyspeed = 2

# create bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# define bullet state
# ready - ready to fire
# fire - bullet is firing

bulletstate = "fire"


# move player left or right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        # place code for sound right here
        bulletstate = "fire"
        # move the bullet right above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# main game loop
while True:
    for enemy in enemies:
        # move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

    # move enemy back and down
    if enemy.xcor() > 280:
        # move all enemies down
        for e in enemies:
            y = e.ycor()
            y -= 40
            # change enemy direction
            enemyspeed *= -1
            e.sety(y)

    if enemy.xcor() < -280:
        # move all enemies down
        for e in enemies:
            y = e.ycor()
            y -= 40
            # change enemy direction
            enemyspeed *= -1
            e.sety(y)

    # check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    # check for a collision between bullet and the enemy
    if isCollision(bullet, enemy):
        # add code for explosion
        # reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        # reset the enemy
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

        # update the score
        score += 10
        scorestring = "Score: %s" % score
        score_pen.clear()
        score_pen.write(scorestring, False, align="left")

    if isCollision(player, enemy):
        # place code for explosion here
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break

    # move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = input("Press enter to finish.")
