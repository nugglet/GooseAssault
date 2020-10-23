import turtle
import random

from libdw import sm

# declare global variables
# score
num = 0
# lives
state = 3
# health state output
output = None
# bullet state
bulstate = 'protec'

# import images
turtle.register_shape('girl.gif')
turtle.register_shape('man.gif')
turtle.register_shape('knoife.gif')
turtle.register_shape('goose.gif')
turtle.register_shape('goose2.gif')

# score counter
counter = turtle.Turtle()
counter.color('yellow')
counter.ht()
counter.penup()
counter.setposition(-150, 310)
counter.write(num, font=('comic Sans MS', 14), align='left')


# define functions
def drawscreen():
    # create playing field
    wn = turtle.getscreen()
    wn.bgcolor('black')
    wn.title('GOOSE ASSAULT')
    wn.bgpic('thebg.gif')
    wn.setup(width=700, height=750)
    steve = turtle.Turtle()
    steve.speed(0)
    steve.color('white')
    steve.penup()
    steve.setposition(-300, -300)
    steve.pendown()
    steve.pensize(3)
    for i in range(4):
        steve.fd(600)
        steve.lt(90)
    steve.ht()

    # create death line
    stove = turtle.Turtle()
    stove.speed(0)
    stove.penup()
    stove.color('purple')
    stove.shape('circle')
    stove.shapesize(0.25)
    stove.setposition(-270, -270)
    for i in range(19):
        stove.stamp()
        x = stove.xcor() + 30
        stove.setx(x)
    stove.ht()

    # create score count ui
    slido = turtle.Turtle()
    slido.speed(0)
    slido.color('white')
    slido.penup()
    slido.setposition(-300, 310)
    score = 'aliens assaulted: '
    slido.write(score, False, align="left", font=("comic Sans MS", 14))
    slido.hideturtle()


def enemycollision(enemy):
    if enemy.ycor() == -270:
        return True
    else:
        return False


def playerbulletcollision(bullet, enemy):
    if bullet.xcor() == enemy.xcor() and bullet.ycor() >= enemy.ycor():
        return True
    else:
        return False


def gameover():
    endscreen = turtle.Screen()
    endscreen.bgcolor('black')

    ghost = turtle.Turtle()
    ghost.color('red')
    ghost.penup()
    ghost.speed(0)
    ghost.write('GAME OVER', move=True, align='center', font=('comic Sans MS', 50))
    ghost.ht()
    return print('GAME OVER')


def win():
    winscreen = turtle.Screen()
    winscreen.bgcolor('white')

    winner = turtle.Turtle()
    winner.penup()
    winner.ht()
    winner.setposition(0, 0)
    winner.write('u win', font=('comic Sans MS', 24), align='left')


def makethingsmove(alien_list, player, health):
    global bulstate
    numalien = len(alien_list)
    dead = []
    while True:

        # animate GOOSE
        player.tortimer.shape('goose2.gif')
        turtle.update()
        player.tortimer.shape('goose.gif')

        # bullet tracking
        if bulstate == 'protec':
            player.spike.bill.ht()
            player.spike.set_position(player.tortimer.xcor(), player.tortimer.ycor() + 30)

        # bullet movement
        if bulstate == 'attac':
            player.spike.bill.st()
            y = player.spike.bill.ycor()
            y += player.spike.speed
            player.spike.bill.sety(y)
            if y >= 280:
                bulstate = 'protec'

        for alien in alien_list:
            # make aliens move 4 grids in 1 sec
            x = alien.isabelle.xcor()
            y = alien.isabelle.ycor()
            x += alien.step
            alien.isabelle.setx(x)

            # set x bounds
            if alien.isabelle.xcor() + alien.step > 270:
                alien.isabelle.setx(270)

            if alien.isabelle.xcor() + alien.step < -270:
                alien.isabelle.setx(-270)

            # if alien hits the edge of screen, move down and reverse direction
            if alien.isabelle.xcor() == 270 or alien.isabelle.xcor() == -270:
                alien.step *= -1

                # set y bound
                if alien.isabelle.ycor() - 60 <= -270:
                    y = -270
                    alien.isabelle.sety(y)
                else:
                    y -= 120
                    alien.isabelle.sety(y)

            # check for collision
            # bullet and enemy + update score
            if playerbulletcollision(player.spike.bill, alien.isabelle) and alien.isabelle.isvisible() \
                    and player.spike.bill.isvisible():
                global num
                alien.isabelle.ht()
                dead.append(alien.isabelle)
                num += 1
                counter.clear()
                counter.write(num, font=('comic Sans MS', 14), align='left')

                if num == numalien:
                    turtle.Screen().clear()
                    win()
                    break

            # player and enemy
            if enemycollision(alien.isabelle) and alien.isabelle.isvisible():
                global state
                state -= 1
                alien.isabelle.ht()
                dead.append(alien.isabelle)
                health.helth(state, player)

        if numalien == len(dead):
            turtle.Screen().clear()
            win()
            break


# Player Class
class Player:
    def __init__(self):
        # create and displayer player turtle
        self.tortimer = turtle.Turtle()
        self.tortimer.color('white')
        self.tortimer.penup()
        self.tortimer.speed(0)
        self.tortimer.setposition(0, -280)
        self.tortimer.setheading(90)
        self.tortimer.shape('goose.gif')

        self.tortispeed = 10

        self.spike = Bullet()
        self.spike.bill.ht()

        # keyboard input
        turtle.listen()
        turtle.onkeypress(self._left, 'Left')
        turtle.onkeypress(self._right, 'Right')
        turtle.onkey(self._controlbullet, 'space')

    def _left(self):
        xl = self.tortimer.xcor()
        if xl - self.tortispeed <= -270:
            xl = -270
        else:
            xl -= self.tortispeed
        self.tortimer.setx(xl)

    def _right(self):
        xr = self.tortimer.xcor()
        if xr + self.tortispeed >= 270:
            xr = 270
        else:
            xr += self.tortispeed
        self.tortimer.setx(xr)

    def _controlbullet(self):  # when spacebar pressed, attac
        global bulstate
        if bulstate == 'protec':
            bulstate = 'attac'


# alien target
class Alien:

    def __init__(self):
        # create enemy sprite
        self.isabelle = turtle.Turtle()
        self.isabelle.color('yellow')
        self.isabelle.shape('man.gif')
        self.isabelle.penup()
        self.isabelle.speed(0)
        self.isabelle.setposition(-270, 270)  # default position 1st grid

        self.step = 5

    def set_position(self, x, y):
        self.isabelle.setposition(x, y)

    def set_speed(self, speed):
        self.step = speed

    def set_col(self, col):
        self.isabelle.color(col)


class GreenAlien(Alien):
    def __init__(self):
        # create enemy sprite
        super().__init__()
        self.isabelle = turtle.Turtle()
        self.isabelle.color('green')
        self.isabelle.shape('girl.gif')
        self.isabelle.penup()
        self.isabelle.speed(0)
        self.isabelle.setposition(-270, 270)  # default position 1st grid

        self.step = 12


# Player Bullet
# Player is given 1 bullet with 2 states
# protec: Bullet tracks player pos
# attac: Bullet is launched forward to hit an enemy then returns back to original position
class Bullet:

    # create bullet sprite
    def __init__(self):
        self.bill = turtle.Turtle()
        self.bill.color('purple')
        self.bill.shape('knoife.gif')
        self.bill.penup()
        self.bill.speed(0)
        self.bill.setheading(90)
        self.bill.shapesize(0.5, 0.5)

        self.speed = 50

    def set_position(self, x, y):
        self.bill.setposition(x, y)

    def xcor(self):
        return self.bill.xcor()

    def ycor(self):
        return self.bill.ycor()


class PlayerHealth(sm.SM):

    def __init__(self):
        self.start_state = 3
        self.hen = turtle.Turtle()
        self.hen.ht()
        self.hen.penup()
        self.hen.color('white')
        self.hen.setposition(300, 310)
        self.string = 'Lives: %s' % self.start_state
        self.hen.write(self.string, font=('comic Sans MS', 14), align='right')

    def helth(self, inp, player):
        global output
        if inp == 3:
            self.string = 'Lives: %s' % inp
            self.hen.write(self.string, font=('comic Sans MS', 14), align='right')
            output = player.tortimer.color('white')
        if inp == 2:
            self.hen.color('orange')
            self.hen.clear()
            self.string = 'Lives: %s' % inp
            self.hen.write(self.string, font=('comic Sans MS', 14), align='right')
            output = player.tortimer.color('orange')
        if inp == 1:
            self.hen.color('red')
            self.hen.clear()
            self.string = 'Lives: %s' % inp
            self.hen.write(self.string, font=('comic Sans MS', 14), align='right')
            output = player.tortimer.color('red')
        if inp == 0:
            turtle.Screen().clear()
            output = gameover()
        return inp, output


def main():
    drawscreen()
    health = PlayerHealth()
    player = Player()
    alien = Alien()
    aliens = [alien]
    # level generator
    for i in range(random.randrange(3, 6)):
        i = Alien()
        x = random.randrange(-270, 270, 30)
        y = random.randrange(210, 300, 30)
        i.set_position(x, y)
        aliens.append(i)

    for i in range(random.randrange(1, 4)):
        i = GreenAlien()
        x = random.randrange(-270, 270, 30)
        y = random.randrange(210, 300, 30)
        i.set_position(x, y)
        aliens.append(i)
    makethingsmove(aliens, player, health)


# main
main()
turtle.mainloop()
