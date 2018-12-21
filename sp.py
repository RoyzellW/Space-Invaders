import turtle
import os
import math
import random

# To make the code and the game my own i need to add a level system and make the bullet balance off of the walls atleast 3 times


# Render sceen
sc = turtle.Screen()
sc.bgcolor("black")
sc.title("Space Invaders")
sc.bgpic("space_invaders_background.gif")

# display shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# this creates the border
border_creater = turtle.Turtle()
border_creater.speed(0)
border_creater.color("white")
border_creater.penup()
border_creater.setposition(-300, -300)
border_creater.pendown()
border_creater.pensize(3)
for side in range(4):
    border_creater.fd(600)
    border_creater.lt(90)
border_creater.hideturtle()

# score
score = 0
score_creater = turtle.Turtle()
score_creater.speed(0)
score_creater.color("white")
score_creater.penup()
score_creater.setposition(-290, 280)
scoreDisplay = "Score: %s" % score
score_creater.write(scoreDisplay, align="left")
score_creater.hideturtle()

# create player
player = turtle.Turtle()
player.shape("player.gif")
# player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# create number of enemies
number_of_enemies = 10
enemies = []
enemy = turtle.Turtle()

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

# add enemies
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


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


def move_Down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)


def move_Up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)


def move_diagonal():
    y = player.ycor()
    x = player.xcor()
    y += playerspeed
    x += playerspeed
    if y > 280:
        y = 280
    if x > 280:
        x = 280
    player.sety(y)
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


# def enemyPosition(enemy, player):
#     if enemy.xcor() or enemy.ycor() > :
#         enemy.hideturtle()


# key bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_Up, "Up")
turtle.onkeypress(move_Down, "Down")
# space has to be lowercased
turtle.onkeypress(fire_bullet, "space")

# tweak out this code
# onkeypress only accepts two parameters
# turtle.onkeypress(move_diagonal, "Right", "Up")

# main game loop
while True:

    if turtle.onkeypress(move_Up, "Up") and turtle.onkeypress(move_Down, "Down"):
        move_diagonal()

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
                e.sety(y)
                # change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                # change enemy direction
            enemyspeed *= -1

        # check for a collision between bullet and the enemy
        if isCollision(bullet, enemy):
            # add code for explosion
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            # bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            enemy.hideturtle()
            # update the score
            score += 10
            scoreDisplay = "Score: %s" % score
            score_creater.clear()
            score_creater.write(scoreDisplay, align="left")

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

# // create a function that checks to see if any eneimes are still on the screen
