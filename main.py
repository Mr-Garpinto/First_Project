#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:02:52 2020

@author: goncalopinto
"""
"""
from PIL import Image  
  
# creating a object  
im = Image.open(r"/Users/goncalopinto/Desktop/bigproject/wof.jpeg")  
  
im.show()
"""

"""
import pygame
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
"""
from level_1 import *
from level_2 import *
from level_3 import *


print("Welcome to the Tarantinos game!")
print("We are super pleased to have you here!")
print("")
input("Press Enter to continue...")
print("")
print("")
print("")
print("")
print("This is a text base game, so keep it in the command line.")
print("If you are using spyder to run this game please open the plots window.")
print("To run this game you need to have pygame package installed on your computer!")
print("")
input("Press Enter to continue...")
print("")
print("")
print("")
print("")
print("")
print("In a bit you'll be asked to chose the theme of the game, addded 3 themes that we find interesting, but I recommend to start with theme 1")
print("")
print("Our game has a couple of challenges, when answering them please try to be as objective as possible with direct answer's")
input("Press Enter to continue...")
print("")
print("")
print("")
print("")
print("Please select the theme for your game!")
print("")
print("")
print("""
      (1)Theme 1 -> IronHack Data Course!
      (2)Theme 2 -> Tarantino Creations!
      (3)Theme 3 -> Nerd Stuff
      """)
print("")


    
theme = input("What would you like to play? ")


while theme not in ["1","2","3"]:
    theme = input("Please select a valid input! (1,2,3) ")

if theme == "1":
    firstlevel()
elif theme == "2":
    secondlevel()
elif theme == "3":
    thirdlevel()
    



#firstlevel()
#secondlevel()
#thirdleve()

"""
img=mpimg.imread('/Users/goncalopinto/Documents/GitHub/First_Project/couch.jpg')
imgplot = plt.imshow(img)
plt.show()


from pygame import mixer


pygame.mixer.init()



explosionSound = mixer.Sound("maybe_next_time.wav")
explosionSound.play()


 #/Users/goncalopinto/Desktop/bigproject/wof.jpg

"""