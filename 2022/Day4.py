'''Part 1'''
# teamCounter = 0
# filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day4.txt"
# with open(filepath, "r") as teams:
#     #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
#     for team in teams:
#         team = team.strip()
#         team = team.replace('-', ',') # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
#         team = team.split(',')
#         # print(team)
#         if (int(team[0]) <= int(team[2]) and int(team[1]) >= int(team[3])) or (int(team[0]) >= int(team[2]) and int(team[1]) <= int(team[3])):
#             print(team)
#             teamCounter += 1
# print(teamCounter)

#Wrong: 819, 359

'''Part 2'''

teamCounter = 0
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day4.txt"
with open(filepath, "r") as teams:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
    for team in teams:
        team = team.strip()
        team = team.replace('-', ',') # https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
        team = team.split(',')
        # print(team)
        if int(team[0]) <= int(team[2]) <= int(team[1]) or int(team[0]) <= int(team[3]) <= int(team[1]) or int(team[2]) <= int(team[0]) <= int(team[3]) or int(team[2]) <= int(team[1]) <= int(team[3]):
            print(team)
            teamCounter += 1
print(teamCounter)

# Wrong: 1000, 834