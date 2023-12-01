
def dataCompiler():
    '''
    Reads the data file, and returns stripped a list with stripped lines
    Returns:
        A list with all the line entries in the data file
    '''
    with open("C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2023/Python/Data/Day1.txt", "r") as r:
        lines = []
        for line in r:
            lines.append(line.strip())
    return lines

def numberExtractor(data):
    '''
    Converts the first & last numbers in each line into a total sum
    Args:
        data: The data for the puzzle
    Returns:
        The total sum value of the first & last numbers in a line
    '''
    sum = 0
    for entry in data:
        numstring = ""
        for char in entry:
            if char.isnumeric():
                numstring += char
                break
        for char in entry[::-1]:
            if char.isnumeric():
                numstring += char
                break
        sum += int(numstring)
    return sum
        

def dataRefiner(data, numbDict):
    '''
    Converts word-letters into (string)digits with first and last letters pre- and appended to them
    Args:
        data: The data for the puzzle
        numbDict: A dictionary with spelled-out numbers and numerical values with first & last letter pre- and appended to them
    Returns:
        a call to numberExtractor with the refined data
    '''
    data_2 = []
    for entry in data:
        for key in numbDict.keys():
            if key in entry:
                entry = entry.replace(key, numbDict[key])
        data_2.append(entry)
    return numberExtractor(data_2)



numbDict = {"one" : 'o1e', "two" : 't2o', "three" : 't3e', "four" : 'f4r', "five" : 'f5e', "six" : 's6x', "seven" : 's7n', "eight" : 'e8t', "nine" : 'n9e'}
data = dataCompiler()
print(numberExtractor(data))
print(dataRefiner(data, numbDict))
