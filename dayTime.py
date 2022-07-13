#This module was made by pascal

import threading
import time
import os

everyCheckpoint = {}
onlyOneThreading = True

def sleepTill(inputtedTime, target = None):
    global onlyOneThreading
    global everyCheckpoint
    splittedTime = inputtedTime.split(":")
    lenghtOfSplits = len(splittedTime)

    #its better printed since it alerts the user
    if lenghtOfSplits == 0 or lenghtOfSplits == 1:
        print("More than 1 number was expected")
    elif lenghtOfSplits > 5:
        print("you got over 5 options")
    else:
        for each in splittedTime:
            if not each.isnumeric():
                print("Numbers were expected")
                return
        
        executedMomment = time.localtime(int(time.time()))


        if lenghtOfSplits == 2:        
            everyCheckpoint[str(executedMomment.tm_year) + ":" + str(executedMomment.tm_mday) + ":" + inputtedTime + ":00"] = target
        elif lenghtOfSplits == 3:
            everyCheckpoint[str(executedMomment.tm_year) + ":" + str(executedMomment.tm_mday) + ":" + inputtedTime] = target
        elif lenghtOfSplits == 4:
            everyCheckpoint[str(executedMomment.tm_year) + ":" + inputtedTime] = target
        elif lenghtOfSplits == 5:
            everyCheckpoint[inputtedTime] = target
            
    if onlyOneThreading == True:
        OffTopic = threading.Thread(target = lambda: checkTime())
        OffTopic.start()
        onlyOneThreading = False
            
    return
    


def checkTime():
    global everyCheckpoint
    while 1:        
        result = time.localtime(int(time.time()))

    #time conversion
    #############################################
        if len(str(result.tm_sec)) == 1:
            seconds = "0" + str(result.tm_sec)
        else:
            seconds = str(result.tm_sec)
            
        if len(str(result.tm_min)) == 1:
            minutes = "0" + str(result.tm_min)
        else:
            minutes = str(result.tm_min)
            
        if len(str(result.tm_hour)) == 1:
            hours = "0" + str(result.tm_hour)
        else:
            hours = str(result.tm_hour)
    #############################################
        
        timeFormat = str(result.tm_year) + ":" + str(result.tm_mday) + ":" + hours + ":" + minutes + ":" + seconds

        del hours, minutes, seconds

        if timeFormat in everyCheckpoint:
            everyCheckpoint[timeFormat]()
            del everyCheckpoint[timeFormat]
            
        del result
        del timeFormat
        time.sleep(1)

        
#testing purposes       
#sleepTill("2022:13:16:48:00")



        
