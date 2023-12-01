'''Part 1'''

# def movement(move, crates):
#     times, start, stop = move[0], move[1]-1, move[2]-1
#     for i in range(times):
#         crates[stop].append(crates[start].pop(-1))
#     return crates
    
# crates = [
# ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
# ['L', 'B', 'N'],
# ['J', 'C', 'H', 'T', 'L', 'V'],
# ['S', 'P', 'J', 'W'],
# ['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
# ['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
# ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
# ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
# ['R', 'P', 'M', 'L', 'H']
# ]

# moves = []
# filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day5.txt"
# with open(filepath, "r") as orders:
#     #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
#     for order in orders:
#         order = order.strip()
#         order = order.replace('move', '') # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
#         order = order.replace('from', '')
#         order = order.replace('to', '')
#         order = order.split()
#         moves.append([int(x) for x in order])
# # print(moves)

# for move in moves:
#     crates = movement(move, crates)

# for stack in crates:
#     print(stack)


'''Part 2'''

def movement(move, crates):
    crateStack, start, stop = move[0], move[1]-1, move[2]-1
    for i in range(-crateStack, 0):
        crates[stop].append(crates[start][i])
    crates[start] = crates[start][:-crateStack]
    return crates

crates = [
['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
['L', 'B', 'N'],
['J', 'C', 'H', 'T', 'L', 'V'],
['S', 'P', 'J', 'W'],
['Z', 'S', 'C', 'F', 'T', 'L', 'R'],
['W', 'D', 'G', 'B', 'H', 'N', 'Z'],
['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'],
['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'],
['R', 'P', 'M', 'L', 'H']
]

moves = []
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day5.txt"
with open(filepath, "r") as orders:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
    for order in orders:
        order = order.strip()
        order = order.replace('move', '') # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
        order = order.replace('from', '')
        order = order.replace('to', '')
        order = order.split()
        moves.append([int(x) for x in order])

for move in moves:
    crates = movement(move, crates)

for stack in crates:
    print(stack)


# lst1 = ['a', 'b', 'c']
# lst2 = [1, 2, 3]

# for i in range(-2, 0):
#     print(lst2[i])
#     lst1.append(lst2[i])
# lst2 = lst2[:-2]

# # lst1.append()
# print(lst1)
# print(lst2)