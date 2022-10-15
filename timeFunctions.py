
import time
import os
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
    file.write(toWrite)
    file.close()

def calcSeconds(input):
    array = input.split(":")
    seconds = int(array[1]) + 60*int(array[0])
    return seconds



def getLargest():

    fileName = "userdata.txt"
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

    print("Largest:" ,largestInt, " ",largestString)


def timer():

    t = 0
    while t<5:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1

    writeData(timer)


timer()
getLargest()