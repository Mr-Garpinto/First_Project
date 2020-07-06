#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 09:07:36 2020

@author: goncalopinto
"""
 #used to pick random quizz
import random  
#used to get mixer thats used with sounds                  
import pygame as py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#import matplotlib.pylab as plt
from pygame import mixer
import matplotlib.image as mpimg
#sound


def secondlevel():
   
    
    #sound for when you find keys
    def sound_keys(x):
        if x == "key for door a":
            py.mixer.init()
            react = mixer.Sound("/Users/goncalopinto/Documents/GitHub/First_Project/key_sound.wav")
            react.play()
        elif x == "key for door b":
            py.mixer.init()
            react = mixer.Sound("/Users/goncalopinto/Documents/GitHub/First_Project/key_sound.wav")
            react.play()
        elif x == "key for door c":
            py.mixer.init()
            react = mixer.Sound("/Users/goncalopinto/Documents/GitHub/First_Project/key_sound.wav")
            react.play()
        elif x == "key for door d":
            py.mixer.init()
            react = mixer.Sound("/Users/goncalopinto/Documents/GitHub/First_Project/game_win_sound.wav")
            react.play()        
    
    
    #define quizz
    #define quizz questions and answer's        
    
    answer_a = {
        "solution":"no",
        "help":["They take too long to film...", "You should ask him!"]
        }
    answer_b = {
        "solution":"yes",
        "help":["Everybody has dreams!", "He wasn't camera friendly"]
        }
    answer_c = {
        "solution":"no",
        "help":["He has a bad earing...", "Do you really think so?"]
        }
    answer_d = {
        "solution":"yes",
        "help":["You can hold so many oscar's...", "Lets say he has his hands full"]
        }
    answer_e = {
        "solution":"no",
        "help":["Did you payed attention to history class...", "You should check wikipedia..."]
        }
    answer_f = {
        "solution":"yes",
        "help":["Those were some caddy's right?", "94' was a great movie year eheheh"]
        }

    
    
    quizzs_s = {
        "Did Tarantino lauch more then 10 movies?" : answer_a,
        "Did Tarantino dreamed of being an actor?" : answer_b,
        "Is audio one of the defining thing in Tarantinos carrear?" : answer_c,
        "Is Tarantino a 2 time oscar winner?" : answer_d,
        "Did the Unglorious Bastards attack really happen in IRL?" : answer_e,
        "Was Pulp Fiction launched in 1994" : answer_f,

        }
    
    #now we need to define the quizz function!
    
    def quizzs():
        
        #pick a random quizzs_s question
        quizz, solution = random.choice(list(quizzs_s.items()))     
        #ask the player for the quizz question answer, and lower the input
        answer = input(quizz + "\n\n" + "Whats the answer to this quizz question?").strip().lower()
        print("")
        n_help = 0
        while answer != solution["solution"]:
            print("")
            help_h = input("Unfortunatly that's the wrong answer, do you really need a hand?").strip().lower()
            if help_h == "yes":
                if n_help < (len(solution["help"])):
                    print("")
                    print(solution["help"][n_help])
                    print("")
                    n_help += 1
                else:
                    print("")
                    print("Bro I said you shouldn't ask for more help....." + "but.. I'll remind you again: ".join(solution["help"]))
                    print("")
                    answer = input(quizz + "\n" + "So, what's the answer to this question?").strip().lower()
                    print("")
            elif help_h == "no":
                print("")
                answer = input(quizz + "\n\n" + "Whats the answer to this quizz question?").strip().lower()
        else:
            if quizz in quizzs_s.keys() and len(quizzs_s.keys()) > 0:
                quizzs_s.pop(quizz)
                print("")
                print("Yeah! I can see that you paid attention to the class!")
                print("")
    
    # photos
    
    #define the photos function
    
    def images(item):
        #for item in items:
           
        if item == "couch":
           
            #ImageAddress = "/Users/goncalopinto/Documents/GitHub/First_Project/couch.jpg"
            img=mpimg.imread('/Users/goncalopinto/Documents/GitHub/First_Project/couch.jpg')
            
        elif item == "piano":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/piano.jpg")
            
        elif item == "fireplace":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/fireplace.jpg")
            
        elif item == "queen bed":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/queen_bed.jpg")
            
        elif item == "safe box":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/safe_box.jpg")
            
        elif item == "double bed":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/double_bed.jpg")
            
        elif item == "dresser":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/dresser.jpg")
            
        elif item == "nightstand":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/nightstand.jpg")
            
        elif item == "dinning table":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/dinning_table.jpg")
            
        elif item == "canvas":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/canvas.jpg")
        
        elif item == "door a":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/door.jpg")
            
        elif item == "door b":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/door.jpg")
            
        elif item == "door c":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/door.jpg")
            
        elif item == "door d":
            img=mpimg.imread("/Users/goncalopinto/Documents/GitHub/First_Project/final_door.jpg")
        
        #img=mpimg.imread(img)
        imgplot = plt.imshow(img)
        plt.show()
        
        """
        ImageItself = Image.open(ImageAddress)
        ImageNumpyFormat = np.asarray(ImageItself)
        plt.imshow(ImageNumpyFormat)
        plt.imshow(ImageNumpyFormat)
        plt.axis('off')
        plt.draw()
        plt.pause(1)
        #plt.close()
        """
        
        """
        img = mpimg.imread(ImageAddress)
        imgplot = plt.imshow(img)
        plt.show()
        """
            
        return
                
            
        
         
    
    
    
    # define things
    
    #interactable objects
    
    canvas = {
        "name": "canvas",
        "type": "furniture",
    }
    
    nightstand = {
        "name": "nightstand",
        "type": "furniture",
    }
    
    safe_box = {
        "name": "safe box",
        "type": "furniture",
    }
    
    fireplace = {
        "name": "fireplace",
        "type": "furniture",
    }
    
    couch = {
        "name": "couch",
        "type": "furniture",
    }
    
    piano = {
        "name": "piano",
        "type": "furniture",
    }
    
    queen_bed = {
        "name": "queen bed",
        "type": "furniture",
    }
    
    double_bed = {
        "name": "double bed",
        "type": "furniture",
    }
    
    dresser = {
        "name": "dresser",
        "type": "furniture",
    }
    
    dining_table = {
        "name": "dining table",
        "type": "furniture",
    }
    
    #doors
    
    
    door_a = {
        "name": "door a",
        "type": "door",
    }
    
    door_b = {
        "name": "door b",
        "type": "door",
    }
    
    door_c = {
        "name": "door c",
        "type": "door",
    }
    
    door_d = {
        "name": "door d",
        "type": "door",
    }
    
    #keys
    
    
    key_a = {
        "name": "key for door a",                           
        "type": "key",
        "target": door_a,
    }
    
    key_b = {
        "name": "key for door b",
        "type": "key",
        "target": door_b,
    }
    
    key_c = {
        "name": "key for door c",
        "type": "key",
        "target": door_c,
    }
    
    key_d = {
        "name": "key for door d",
        "type": "key",
        "target": door_d,
    }
    
    #rooms
    
    game_room = {
        "name": "game room",
        "type": "room",
    }
    
    outside = {
      "name": "outside"
    }
    
    bedroom1 = {
        "name": "bedroom 1",
        "type": "room",
        
    }
    
    bedroom2 = {
        "name": "bedroom 2",
        "type": "room",
        
    }
    
    living_room = {
        "name": "living room",
        "type": "room",
        
    }
    
    
    
    
    
    all_rooms = [game_room, outside, bedroom1, bedroom2, living_room]
    
    all_doors = [door_a, door_b, door_c, door_d]
    
    # define relations between things
    object_relations = {
        "game room": [couch, piano,fireplace, door_a],
        "fireplace": [key_a],
        "outside": [door_d],
        "door a": [game_room, bedroom1],
        "door b": [bedroom1, bedroom2],
        "door c": [bedroom1, living_room],
        "door d": [living_room, outside],
        "bedroom 1": [queen_bed,safe_box, door_a, door_b, door_c],
        "safe box": [key_b],
        "bedroom 2": [double_bed, dresser,nightstand, door_b],
        "nightstand": [key_c],
        "canvas": [key_d],
        "living room": [dining_table, canvas, door_c, door_d]
    }
    
    # define game state. Do not directly change this dict. 
    # Instead, when a new game starts, make a copy of this
    # dict and use the copy to store gameplay state. This 
    # way you can replay the game multiple times.
    
    INIT_GAME_STATE = {
        "current_room": game_room,
        "keys_collected": [],
        "target_room": outside
    }
    
    def linebreak():
        """
        Print a line break
        """
        print("\n\n")
    
    def start_game():
        """
        Start the game
        """
        print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
        play_room(game_state["current_room"])
    
    def play_room(room):
        """
        Play a room. First check if the room being played is the target room.
        If it is, the game will end with success. Otherwise, let player either 
        explore (list all items in this room) or examine an item found here.
        """
        game_state["current_room"] = room
        if(game_state["current_room"] == game_state["target_room"]):
            print("Congrats! You escaped the room!")
        else:
            print("")
            print("You are now in " + room["name"])
            print("")
            intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip().lower()
            if intended_action == "explore":
                explore_room(room)
                play_room(room)
            elif intended_action == "examine":
                examine_item(input("What would you like to examine?").strip().lower())
            else:
                print("Not sure what you mean. Type 'explore' or 'examine'.")
                play_room(room)
            linebreak()
    
    def explore_room(room):
        """
        Explore a room. List all items belonging to this room.
        """
        items = [i["name"] for i in object_relations[room["name"]]]
        print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))
    
    def get_next_room_of_door(door, current_room):
        """
        From object_relations, find the two rooms connected to the given door.
        Return the room that is not the current_room.
        """
        connected_rooms = object_relations[door["name"]]
        for room in connected_rooms:
            if(not current_room == room):
                return room
    
    def examine_item(item_name):
        """
        Examine an item which can be a door or furniture.
        First make sure the intended item belongs to the current room.
        Then check if the item is a door. Tell player if key hasn't been 
        collected yet. Otherwise ask player if they want to go to the next
        room. If the item is not a door, then check if it contains keys.
        Collect the key if found and update the game state. At the end,
        play either the current or the next room depending on the game state
        to keep playing.
        """
        current_room = game_state["current_room"]
        next_room = ""
        output = None
        
        for item in object_relations[current_room["name"]]:
            if(item["name"] == item_name):
                print("")
                output = "You examine " + item_name + ". "
                print("")
                images(item_name) #im testing this out to see if I'm able to put the images working yayyy....
                if(item["type"] == "door"):
                    have_key = False
                    for key in game_state["keys_collected"]:
                        if(key["target"] == item):
                            have_key = True
                    if(have_key):
                        print("")
                        output += "You unlock it with a key you have."
                        print("")
                        next_room = get_next_room_of_door(item, current_room)
                    else:
                        print("")
                        output += "It is locked but you don't have the key."
                else:
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        print("")
                        print("So that you could gaind access to this key, you first need to answer me to this question!")
                        print("")
                        quizzs()
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                        sound_keys(item_found["name"])
                    else:
                        output += "There isn't anything interesting about it."
                        print("")
                print(output)
                break
    
        if(output is None):
            print("")
            print("The item you requested is not found in the current room.")
            print("")
        
        if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip().lower() == 'yes'):
            play_room(next_room)
        else:
            play_room(current_room)
            
    py.mixer.init()
    react = mixer.Sound("/Users/goncalopinto/Documents/GitHub/First_Project/piano.wav")
    react.play()
    
    game_state = INIT_GAME_STATE.copy()
    
    start_game()
    