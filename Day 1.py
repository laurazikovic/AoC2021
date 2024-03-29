"""
@author: laura.zikovic
AoC 2021,Day 1 - Sonar Sweep - optimizirano
"""
input_data = open("Inputday1.txt").read().split("\n")
#print(type(input_data[1]))
int_input_data = [int(i) for i in input_data]

#koji je broj onih koji su > od previous
def first(d=int_input_data):
    return sum(1 if d[i-1] < d[i] else 0 for i in range(len(d)))

#consider sum of a three-measurement sliding window (i-2, i-1, i-2)- use first()
def second(d=int_input_data):
    return first([d[i-2] + d[i - 1] + d[i] for i in range(len(d)) if i >= 2]) #sum(d[i-2:i])

print(f"Solution of the 1st part: {first()}\nSolution of the 2nd part: {second()}")
