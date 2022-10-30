import tkinter
from tkinter import *
import random

choice = 0
rps_list = ["rock", "paper", "scissors"]

#Defining the bumper presses with the V5 brain
def bumper_a_press():
    global choice
    brain.screen.print("You chose rock")
    brain.screen.next_row()
    choice = 1
    wait(2, SECONDS)

def bumper_b_press():
    global choice
    brain.screen.print("You chose paper")
    brain.screen.next_row()
    choice = 2
    wait(2, SECONDS)

def bumper_c_press():
    global choice
    brain.screen.print("You chose scissors")
    brain.screen.next_row()
    choice = 3
    wait(2, SECONDS)

bumper_a.pressed(bumper_a_press)
bumper_b.pressed(bumper_b_press)
bumper_c.pressed(bumper_c_press)

#Main code chunk (highly unoptomized)
while True:
    #Establishing what the computer picks everytime the loop runs
    rps_choice = random.choice(rps_list)
    choice = 0
    while not choice:
        wait(0.01, SECONDS)
    brain.screen.print("I choose", rps_choice)
    brain.screen.next_row()

    #Logic that determines who wins and prints that to the V5 screen
    if rps_choice == "scissors" and choice == 1:
        brain.screen.print("You win!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "scissors" and choice == 2:
        brain.screen.print("You lose...")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "scissors" and choice == 3:
        brain.screen.print("It's a draw!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "rock" and choice == 1:
        brain.screen.print("It's a draw!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "rock" and choice == 2:
        brain.screen.print("You win!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "rock" and choice == 3:
        brain.screen.print("You lose...")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "paper" and choice == 1:
        brain.screen.print("You lose...")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "paper" and choice == 2:
        brain.screen.print("It's a draw!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
    elif rps_choice == "paper" and choice == 3:
        brain.screen.print("You win!")
        wait(2, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1,1)
        continue
#An unfinished attempt at making the GUI to allow playing without a V5 brain
'''top = tkinter.Tk()

def button_a_press():
    tkinter.messagebox.showinfo("Hello Python", "Hello World")

B = tkinter.Button(top, text = "Rock", command = button_a_press)

B.pack()
top.mainloop()'''
