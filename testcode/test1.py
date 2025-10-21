from LoofahLib import *

pause(roll(1,5))
save(r"C:\Users\mabre\OneDrive\Desktop\code folder\python\custommodulesyayyyy\save.json", "hello there")
say("Successfully loaded save, contains data:" + str(load(r"C:\Users\mabre\OneDrive\Desktop\code folder\python\custommodulesyayyyy\save.json")))
