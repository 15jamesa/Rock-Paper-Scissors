from appJar import gui
import random

def decision(btn):
    selection = ["Rock", "Paper", "Scissors"]
    comp = random.choice(selection)
    result = ("You chose:", btn, "The computer chose:", comp)
    rps.setLabel("Results", result)
    if (btn=="Rock" and comp=="Scissors") or (btn=="Paper" and comp=="Rock") or (btn=="Scissors" and comp=="Paper"):
        rps.setLabel("Instructions", "Player wins!")
    elif (comp=="Rock" and btn=="Scissors") or (comp=="Paper" and btn=="Rock") or (comp=="Scissors" and btn=="Paper"):
        rps.setLabel("Instructions", "Computer wins!")
    else:
        rps.setLabel("Instructions", "It's a tie!")


rps = gui("Rock, Paper, Scissors", "400x250")

rps.addLabel("Instructions", "Choose either Rock, Paper, or Scissors:", 1, 0, 4)
rps.addLabel("Results", "", 0, 0, 4)

rps.addButton("Rock", decision, 2, 0)
rps.addButton("Paper", decision, 2, 1)
rps.addButton("Scissors", decision, 2, 2)

rps.go()
