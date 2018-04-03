"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def input_score():
        global score
        score = float(input("Enter score: "))


input_score()
if score <= 0:
        print("Invalid score")
elif score >= 100:
        print("Invalid score")
if score > 50 and score < 90 :
        print("Passable")
if score > 90 and score < 100 :
        print("Excellent")
if score > 0 and score < 50:
        print("Bad")