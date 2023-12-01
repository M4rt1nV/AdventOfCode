'''Part 1'''

total_calories = 0
Calories_List = []
filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day1.txt"
with open(filepath, "r") as calories:
    #Loopt door alle regels in de woordenlijst https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
    for line in calories:
        if line.strip() == "":
            Calories_List.append(total_calories)
            total_calories = 0
            continue
        total_calories += int(line.strip())
print(max(Calories_List))


'''Part 2'''

Calories_List.sort()
print(Calories_List)
print(f"{Calories_List[-1]} + {Calories_List[-2]} + {Calories_List[-3]} = {Calories_List[-1] + Calories_List[-2] + Calories_List[-3]}")