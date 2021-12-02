"""
@author: laura.zikovic
AoC 2021,Day 2 - Dive!
"""
#Razdvojiti smjerove od vrijednosti i za svaki string u jednoj listi sa zadanim uvjetom na istom mjestu u drugoj listi određujem operaciju
from functools import reduce

directions = []
values = []
depth= 0
hor = 0
aim = 0

with open("Inputday2.txt","r") as input_data:
    for el in input_data:
        direction = el.split()[::2]
        directions.append(direction)
with open("Inputday2.txt","r") as input_data:
    for el2 in input_data:
        value = el2.split()[1::2]
        values.append(list(map(int, value)))        #int!!???
int_values = reduce(lambda x,y: x+y, values)

#1st part: Postavljam se u horizontalnu ravninu x i y(d), gdje u +smjeru idem prema dolje (depth+)
for (a, b) in zip(directions[0::1], int_values[0::1]):  #prvi put sam koristila zip :D
    if a == ["down"]:
        depth += b
    elif a == ["up"]:
        depth -= b
    else:
        hor += b
#print(directions[1] == ['down']) #check if it is true
print(f"Solution of the 1st part: {hor*depth}")

depth= 0    #refresh
hor = 0
#2nd part 
for (a, b) in zip(directions[0::1], int_values[0::1]):
    if a == ["down"]:
        aim += b
    elif a == ["up"]:
        aim -= b
    else:
        hor += b
        depth += b*aim

print(f"Solution of the 2nd part: {hor*depth}")
