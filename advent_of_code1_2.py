# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:34:49 2021

@author: Emilie
"""
from bisect import bisect

f = open("C:/Users/37129/Desktop/positions.txt", "r")

horizontali = 0
dzilums = 0
aim = 0

# for x in f:
#     a,b = x.split()
#     b = int(b)
#     if a == 'forward':
#         horizontali = horizontali + b
#     if a == 'up':
#         dzilums = dzilums - b
#     if a == 'down':
#         dzilums = dzilums + b

# y = dzilums*horizontali
# print(y)
        
for x in f:
    a,b = x.split()
    b = int(b)
    if a == 'forward':
        horizontali = horizontali + b
        dzilums = dzilums + aim*b
    if a == 'up':
        aim = aim - b
    if a == 'down':
        aim = aim + b
        
y = dzilums*horizontali
print(y)
        
    
# f = open("C:/Users/37129/Desktop/cipari.txt", "r")
# cipari = []
# for x in f:
#     cipari.append(int(x)) 

# izmaina = []
# c = 0
# for i in range(0, len(cipari)-1):
#     y = cipari[i+1] - cipari[i]
#     if y > 0:
#         c = c + 1
#     izmaina.append(y)

# a = 0
# b = 0
# c = 0
# for i in range(0, len(cipari)-3):
#     a = cipari[i] + cipari[i+1] + cipari[i+2]
#     b = cipari[i+1] + cipari[i+2] + cipari[i+3]
#     y = b - a
#     if y > 0:
#         c = c + 1




    