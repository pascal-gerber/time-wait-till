import dayTime

def say(test):
    print(test)

dayTime.sleepTill("19:10:00", target = lambda: say("test1"))

dayTime.sleepTill("19:10:05", target = lambda: say("test2"))

