# 9/17/2025

"""
Write a python program that calculates the average of 3 scores of a team 
and displays the result. Make sure to get the scores from the user on the terminal.
"""
# getting team name from the user

team = input("enter the team name: ")

# getting the score 1 from the user
# We cast (do conversation) the user inputs as strings into numbers-integers

score1 = int(input("Enter the first score:"))
score2 = int(input("Enter the second score:"))
score3 = int(input("Enter the third score:"))

avg = (score1 + score2 + score3) / 3
print("The team", team, "had an average score of", round(avg, 2) ) 


# when using the rounds function the number determines what decimal point it rounds to

# by deafult user inputs are strings