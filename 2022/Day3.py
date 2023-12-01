'''Part 1'''

prioritySum = 0
prio_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

# filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day3.txt"
# with open(filepath, "r") as rucksacks:
#     #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
#     for contents in rucksacks:
#         contents = contents.strip()
#         compartmentSize = int((len(contents) / 2))
#         compartment1 = contents[:compartmentSize]
#         print(len(compartment1))
#         compartment2 = contents[compartmentSize:]
#         print(len(compartment2))
#         print(f"{contents} = {compartment1} + {compartment2}")
#         item = "unfound"
#         while item == "unfound":
#             for item in compartment1:
#                 if item in compartment2:
#                     print(item)
#                     prioritySum += prio_dict[item]
#                     item = "found"
#                     break
            
print(prioritySum)
# Wrong: 17923, 7666

'''Part 2'''

contentsList = []
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day3.txt"
with open(filepath, "r") as rucksacks:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
    for contents in rucksacks:
        contentsList.append(contents.strip())
print(contentsList)

for i in range(0, len(contentsList), 3):
    bag1 = contentsList[i]
    bag2 = contentsList[i + 1]
    bag3 = contentsList[i + 2]
    for item in bag1:
        if item in bag2 and item in bag3:
            prioritySum += prio_dict[item]
            break
print(prioritySum)


# Wrong: 3821