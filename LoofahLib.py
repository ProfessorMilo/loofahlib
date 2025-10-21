# og concept = mloeimnfag
# og concept expanded = massive library of everything i might need for a game
# draft 1 expanded = library of modules for games
# draft 1 = lomfg
# replace m with o = loofg
# replace g with a = loofa
# add lib to the end = loofahlib
# final name = loofahlib


import random
import math
import time
import pygame
import json
import os
from playsound import playsound

def pause(seconds=1):
    time.sleep(seconds)

def roll(min_val, max_val):
    return random.randint(min_val, max_val)

def say(msg):
    print(f"[Game] {msg}")

def save(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load(file, default=None):
    if not os.path.exists(file):
        print(f"[LoofahLib] Save file not found, returning default.")
        return default
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print(f"[LoofahLib] Error reading {file}, returning default.")
            return default
def playloop(sound, repeat=1):
    for _ in range(repeat):
        playsound(sound)



pause(roll(1,5))
save(r"C:\Users\mabre\OneDrive\Desktop\code folder\python\custommodulesyayyyy\save.json", "hello there")
say("Successfully loaded save, contains data:" + str(load(r"C:\Users\mabre\OneDrive\Desktop\code folder\python\custommodulesyayyyy\save.json")))
