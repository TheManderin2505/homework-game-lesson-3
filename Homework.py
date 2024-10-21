import pgzrun
from random import randint
import time

WIDTH = 600
HEIGHT = 600
TITLE = "Fighter jet game"

player = Actor('alien')
computer = Actor('alien_2')
lazer1 = Actor('lazer1')
player.pos = 300,450
computer.pos = 300, 50


def move_comp():
    computer.x=randint(50,450)
    computer.y=randint(50,300)

def update():
    if keyboard.A:
        player.x -= 5
    elif keyboard.D:
        player.x += 5
    



def on_mouse_down():
    lazer1.pos = player.pos
    for i in range(50):
      lazer1.y -= 10
      if lazer1.colliderect(computer):
         move_comp()


    




#.colliderect()


def draw():
    screen.clear()
    screen.fill("light blue")
    player.draw()
    computer.draw()
    lazer1.draw()


#move_comp()









pgzrun.go()