import dayTime
import time

def say(test):
    print(test)

dayTime.sleepTill("18:49:00", target = lambda: say("fuck you reb"))
dayTime.sleepTill("18:49:05", target = lambda: say("fuck you dave"))

