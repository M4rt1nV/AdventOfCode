'''Part 1'''

# def game(rival, me):
#     if (rival == 'A' and me == 'X') or (rival == 'B' and me == 'Y') or (rival == 'C' and me == 'Z'):
#         return 'draw'
#     if (rival == 'A' and me == 'Y') or (rival == 'B' and me == 'Z') or (rival == 'C' and me == 'X'):
#         return 'win'
#     if (rival == 'A' and me == 'Z') or (rival == 'B' and me == 'X') or (rival == 'C' and me == 'Y'):
#         return 'loss'


# rps = []
# filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day2.txt"
# with open(filepath, "r") as calories:
#     #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
#     for line in calories:
#         rps.append((line.strip()[0], line.strip()[2]))

# pointsDict = {'X': 1, 'Y': 2, 'Z': 3, 'win': 6, 'draw': 3, 'loss': 0}
# score = 0

# for match in rps:
#     result = game(match[0], match[1])
#     score += pointsDict[result] + pointsDict[match[1]]

# print(score)


'''
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors
'''

'''Part 2'''

def game(rival, result):
    if result == 'X':
        if rival == 'A':
            return 'Scissors'
        elif rival == 'B':
            return 'Rock'
        elif rival == 'C':
            return 'Paper'
    
    if result == 'Y':
        if rival == 'A':
            return 'Rock'
        elif rival == 'B':
            return 'Paper'
        elif rival == 'C':
            return 'Scissors'
    
    if result == 'Z':
        if rival == 'A':
            return 'Paper'
        if rival == 'B':
            return 'Scissors'
        if rival == 'C':
            return 'Rock'

rps = []
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day2.txt"
with open(filepath, "r") as calories:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
    for line in calories:
        rps.append((line.strip()[0], line.strip()[2]))

pointsdict = {'X': 0, 'Y': 3, 'Z': 6, 'Rock': 1, 'Paper': 2, 'Scissors': 3}
score = 0

for match in rps:
    move = game(match[0], match[1])
    score += pointsdict[move] + pointsdict[match[1]]

print(score)


'''
A = Rock
B = Paper
C = Scissors

X = Loss
Y = Draw
Z = Win
'''