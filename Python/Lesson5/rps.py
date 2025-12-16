import sys
print("")
playerchoice = input("Enter...\n 1 for Rock, \n 2 for Paper ,or \n 3 for Scissors:\n\n")

if playerchoice < 1 | playerchoice >3:
  sys.exit("You must Enter 1,2,3.")