def dataCompiler():
    '''
    Reads the data, splits it in lines and checks
    '''
    with open("C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2023/Data/Day2.txt", "r") as r:
        games = {}
        for line in r:
            line = line.strip()
            line = line.split(":")
            gameNumb = line[0].split(" ")
            gameNumb = gameNumb[1]
            line[1] = line[1].split(";")
            games[gameNumb] = colourCalc(line[1])
    return games

def colourCalc(data):
    '''
    Splits a list of draws and accumulates the total number of draws of every colour
    Args:
        data: A list of draws
    Returns:
        A dict with the highest draws of each colour
    '''
    colourDict = {'green' : 0, 'red' : 0, 'blue' : 0}
    # print(data)
    for draw in data:
        colourDraw = {'green' : 0, 'red' : 0, 'blue' : 0}
        draw = draw.split(",")
        for colour in draw:
            colour = colour.lstrip()
            colour = colour.split(" ")
            colourDraw[colour[1]] += int(colour[0])
        # print(colourDraw)
        for colour in colourDraw:
            if colourDraw[colour] > colourDict[colour]:
                colourDict[colour] = colourDraw[colour]
    return colourDict

def datafit(data):
    total = 0
    maxDict = {'green' : 13, 'red' : 12, 'blue' : 14}
    for game in data:
        if data[game]['green'] <= maxDict['green']:
            if data[game]['red'] <= maxDict['red']:
                if data[game]['blue'] <= maxDict['blue']:
                    total += int(game)
    return total

def datamin(data):
    total = 0
    for game in data:
        cubepower = data[game]['green'] * data[game]['red'] * data[game]['blue']
        total += cubepower
    return total


data = dataCompiler()
print(datafit(data))
print(datamin(data))
