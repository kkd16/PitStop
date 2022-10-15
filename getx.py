file = open("facts.txt")

def getX(line):
    line_width = 0
    for char in line:
        line_width += 6

    diff = 394 - line_width
    x = diff / 2
    return x


  