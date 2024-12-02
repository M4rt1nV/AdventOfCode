def dataCompiler():
    '''
    Reads the data file, and returns stripped a list with stripped lines
    Returns:
        A list with all the line entries in the data file
    '''
    with open("C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2024/Data/Day1.txt", "r") as r:
        lines = []
        for line in r:
            lines.append(line.strip())
    return lines

def dataStripper(data):
    rlist = []
    llist = []
    for entry in data:
        split = entry.split("   ")
        rlist.append(int(split[1]))
        llist.append(int(split[0]))
    rlist.sort()
    llist.sort()
    return rlist, llist

def dataCalc1(rlist, llist):
    total = 0
    for i in range(len(rlist)):
        if rlist[i] > llist[i]:
            dist = rlist[i] - llist[i]
            total += dist
        elif rlist[i] < llist[i]:
            dist = llist[i] - rlist[i]
            total += dist
        else:
            total += 0
    print(total)

def dataCalc2(rlist, llist):
    similarityScore = 0
    for lnum in llist:
        multiplier = 0
        for rnum in rlist:
            if lnum == rnum:
                multiplier += 1
        similarityScore += (lnum * multiplier)
    print(similarityScore)






data = dataCompiler()
rlist, llist = dataStripper(data)

dataCalc1(rlist, llist)
dataCalc2(rlist, llist)