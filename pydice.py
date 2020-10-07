#!/usr/bin/python3

import random

# declare dictionary to store number of dice to be rolled
rollDict = {}

# print welcome
print("\n *** Welcome to pydice! *** ")
print("\n Input the number of each dice you wish to roll, or press enter to skip!")
print("\n")

# get user input for dice to be rolled
for i in [4,6,8,10,12,20]:
    rollDict.update({ i: input("d" + str(i) + "s: ")})

total = 0

# calculate and print rolls
for key in rollDict:
    if rollDict[key] != 0 and rollDict[key] != '':
        print("\n * d" + str(key) + " *")
        throwsum = 0
        for i in range(int(rollDict[key])):
            throw = random.randint(1,int(key))
            print("#" + str(i+1) + " - " + str(throw))
            total = total + throw
            throwsum = throwsum + throw
        #print total for this dice
        print("d" + str(key) + " total: " + str(throwsum))

# print total
if total != 0:
    print("\n *** Total: " + str(total) + " ***")
else:
    print("\n NO DICE ROLLED!")
