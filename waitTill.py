import time

def waituntill(Time):
    now = 1655244000
    otherNow = int(time.time())

    now = otherNow - now

    while now > 86400:
        now -= 86400

    Cuttime = Time.split(":")
    
    if len(Cuttime) == 3:
        WaitTime = int(Cuttime[0]) * 3600 + int(Cuttime[1]) * 60 + int(Cuttime[2])
    elif len(Cuttime) == 2:
        WaitTime = int(Cuttime[0]) * 3600 + int(Cuttime[1]) * 60
    elif len(Cuttime) == 1:
        WaitTime = int(Cuttime[2])
    elif len(Cuttime) == 4:
        WaitTime = int(Cuttime[0]) * 86400 + int(Cuttime[1]) * 3600 + int(Cuttime[2]) * 60 + int(Cuttime[3])
    
    return(WaitTime - now)
    
             
