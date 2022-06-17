import time

def waituntill(Time):
    now = 1655244000
    otherNow = int(time.time())

    now = otherNow - now

    while now > 86400:
        now -= 86400

    Cuttime = Time.split(":")

    Error = False
    
    if len(Cuttime) == 1: #do your own time in seconds directly (you have to calculate manually)
        WaitTime = int(Cuttime[0])
    elif len(Cuttime) == 2: #takes hours and minutes like "12:30", waits till "12:30"
        WaitTime = int(Cuttime[0]) * 3600 + int(Cuttime[1]) * 60
    elif len(Cuttime) == 3: #takes hours, minutes and seconds "12:30:10", waits till "12:30:10"
        WaitTime = int(Cuttime[0]) * 3600 + int(Cuttime[1]) * 60 + int(Cuttime[2])
    elif len(Cuttime) == 4: #takes days with specific commands on choice "1:12:30:00", waits till tomorow at "12:30"
        WaitTime = int(Cuttime[0]) * 86400 + int(Cuttime[1]) * 3600 + int(Cuttime[2]) * 60 + int(Cuttime[3])
    elif len(Cuttime) == 0:
        Error = True
        raise TypeError("Expected a time")
    else:
        Error = True
        raise TypeError("More than 4 options detected, did you mean:" +
                        Cuttime[-3] + ":" + Cuttime[-2] + ":" + Cuttime[-1] + "?")

    if Error == False:
        return(WaitTime - now)

#note: i programmed it purposefully so it can take way more than just example 60 seconds,
#you can add as many seconds you want. 
#it takes the beginning of today and adds all the userOptions to the start of the day in seconds.
#Note: if theres any issue, contact me about it.

#Made by Pascal
            
