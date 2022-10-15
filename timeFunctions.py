import os
import math
from datetime import date

def writeData(endTime):

    fileName = "userdata.txt"
    file = open(fileName, "a")
    filesize = os.path.getsize(fileName)
    todaysDate = date.today().strftime('%Y-%m-%d')
    toWrite = ""

    if filesize != 0:
       toWrite = "#" + toWrite

    toWrite = toWrite + todaysDate + "+"  + endTime
    print("Writing Data: ", toWrite + "\n")
    file.write(toWrite)
    file.close()

def calcSeconds(input):
    array = input.split(":")
    seconds = int(array[1]) + 60*int(array[0])
    return seconds

def convertSecsToString(input):
    mins = math.floor(input/60)
    secs = math.floor(input % 60)
    ret = '{:02d}:{:02d}'.format(mins, secs)
    return ret

def getLargest():
    fileName = "userdata.txt"
    filesize = os.path.getsize(fileName)

    if filesize==0:
        return "No poops yet!"
    file = open(fileName, "r")
    
    string = file.read()
    array = string.split("#")

    largestInt = -1
    largestString = ""

    for entry in array:
        array = entry.split("+")
        secs = calcSeconds(array[1])
        if (secs > largestInt):
            largestInt = secs
            largestString = entry

    file.close()
    largestArray = largestString.split("+")
    return "Your worst time was " + largestArray[1] + " on " + largestArray[0] + "."

def getFastest():

    fileName = "userdata.txt"
    filesize = os.path.getsize(fileName)

    if filesize==0:
        return "No poops yet!"
    file = open(fileName, "r")
    
    string = file.read()
    array = string.split("#")

    smallestInt = 9999999999999
    smallestString = ""

    for entry in array:
        array = entry.split("+")
        secs = calcSeconds(array[1])
        if (secs < smallestInt):
            smallestInt = secs
            smallestString = entry

    file.close()
    smallestArray = smallestString.split("+")
    return "Your best time was " + smallestArray[1] + " on " + smallestArray[0] + "."

def getAverage():

    fileName = "userdata.txt"
    filesize = os.path.getsize(fileName)

    if filesize==0:
        return "No poops yet!"
    file = open(fileName, "r")
    
    string = file.read()
    array = string.split("#")

    avgInt = 0
    i = 0
    for entry in array:
        array = entry.split("+")
        secs = calcSeconds(array[1])
        avgInt = avgInt + secs
        i = i + 1
    
    avgInt = avgInt/i
    
    ret = convertSecsToString(avgInt)

    file.close()
    return "Your average poo time is " + ret + "."

# Writes data
# Returns Difference from last poo
def stop(endTime):

    fileName = "userdata.txt"
    filesize = os.path.getsize(fileName)
    
    if (filesize==0):
        writeData(endTime)
        return "This was your first poo!"

    writeData(endTime)
    file = open(fileName, "r")
    stringArray = file.read().split("#")
    file.close()
    previousSeconds = calcSeconds(stringArray[-2].split("+")[1])
    currentSeconds = calcSeconds(stringArray[-1].split("+")[1])

    # scored a worse time
    if (currentSeconds > previousSeconds):
        difference = currentSeconds - previousSeconds
        ret = convertSecsToString(difference)
        return "Slower than last time by " + ret + " :("

    # scored a better time
    if (currentSeconds < previousSeconds):
        difference = previousSeconds - currentSeconds
        ret = convertSecsToString(difference)
        return "Faster than last time by " + ret + " :)"

    if (currentSeconds == previousSeconds):
        return "Same speed as last time."


