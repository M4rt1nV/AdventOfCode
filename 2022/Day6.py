'''Part 1'''

filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day6.txt"
with open(filepath, "r") as message:
    for line in message:
        msg = line.strip()
for i in range(4, len(msg)+1):
    key = set(msg[i-4:i])
    if len(key) == 4:
        print(i)
        print(key)
        break
# Wrong: 1832 (Low),

'''Part 2'''

filepath = "C:/Users/marti/Dropbox/Hacklab/AdventOfCode/2022/Python/Data/Day6.txt"
with open(filepath, "r") as message:
    for line in message:
        msg = line.strip()
for i in range(14, len(msg)+1):
    key = set(msg[i-14:i])
    if len(key) == 14:
        print(i)
        print(key)
        break
