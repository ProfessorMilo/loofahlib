from LoofahLib import *

pause(roll(1,5))
save(r"save.json", "hello there")
say("Successfully loaded save, contains data:" + str(load(r"save.json")))
