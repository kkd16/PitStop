file = open("facts.txt")

def getWidth(line):
    line_width = 0
    for char in line:
        line_width += 6
    return line_width

def getlineX():
    width = getWidth(line)
    diff = 394 - width
    x = diff / 2
    return x

for line in file:
    x = getlineX()
    #print(x)
  