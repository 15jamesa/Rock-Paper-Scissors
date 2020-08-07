from appJar import gui
import random

def decision(btn):
    selection = ["Rock", "Paper", "Scissors"]
    comp = random.choice(selection)
    result = "You chose: " + btn + "\n\nThe computer chose: " + comp
    rps.setLabel("Instructions", result)
    if (btn=="Rock" and comp=="Scissors") or (btn=="Paper" and comp=="Rock") or (btn=="Scissors" and comp=="Paper"):
        rps.setLabel("Results", "Player wins!")
    elif (comp=="Rock" and btn=="Scissors") or (comp=="Paper" and btn=="Rock") or (comp=="Scissors" and btn=="Paper"):
        rps.setLabel("Results", "Computer wins!")
    else:
        rps.setLabel("Results", "It's a tie!")

def refresh():
    rps.setLabel("Instructions", "Choose either Rock, Paper, or Scissors:")
    rps.setLabel("Results", "")

def blank():
    pass


rps = gui("Rock, Paper, Scissors", "600x250")

rps.addLabel("Results", "", 1, 0, 4)
rps.addLabel("Instructions", "Choose either Rock, Paper, or Scissors:", 0, 0, 4)
rps.setSticky("nesw")
rps.setBg("Azure", override=False)

rps.addButton("Rock", decision, 2, 0)
rps.addButton("Paper", decision, 2, 1)
rps.addButton("Scissors", decision, 2, 2)
rps.addButton("Refresh", refresh, 3, 1)
rps.addButton("", blank, 3, 0)
rps.addButton(" ", blank, 3, 2)

rps.setButtonBg("Rock", "HoneyDew")
rps.setButtonBg("Paper", "HoneyDew")
rps.setButtonBg("Scissors", "HoneyDew")
rps.setButtonBg("Refresh", "HoneyDew")
rps.setButtonBg("", "HoneyDew")
rps.setButtonBg(" ", "HoneyDew")

rps.go()
