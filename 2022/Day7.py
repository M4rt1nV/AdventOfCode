'''Part 1'''
directoryDict = {}
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day7.txt"
with open(filepath, "r") as message:
    for line in message:
        print(line.strip())
        if "$" in line:
            line = line.strip()
            line = line.split()
            if ".." not in line:
                try:
                    directoryDict[line[2]] = 0
                except(IndexError):
                    pass
        # if "$" not in line:
        #     line = line.strip()
        #     line = line.split()
        #     print(line)
print(directoryDict)
