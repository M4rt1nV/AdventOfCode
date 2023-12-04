def dataRead():
    data = []
    with open("C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2023/Data/Day3.txt", "r") as r:
        for line in r:
            data.append(list(line.strip()))
    return data

def symbolFind(data):
    symbollist = "!@#$%^&*()_-+={}[]"
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isnumeric():
                for k in range(j, len(data[i])):
                    indexList = []
                    if data[i][k].isnumeric():
                        indexList.append(k)
                    elif data[i][k] == '.':
                        break
                
                if i > 0:
                    if j > 0:                
                        pass    
                # print(data[i][j])

def numbCreate(data, indexes):
    pass
            

    # pass



data = dataRead()
symbolFind(data)