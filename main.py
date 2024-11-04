import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Rock, Paper, Scissors")

ROCK = tk.PhotoImage(file='rock.png')
PAPER = tk.PhotoImage(file='paper.png')
SCISSORS = tk.PhotoImage(file='scissors.png')

images = {
    'rock': ROCK,
    'paper': PAPER,
    'scissors': SCISSORS
}

player_label = tk.Label(root, image=ROCK)
computer_label = tk.Label(root, image=ROCK)

player_label.grid(row=0, column=0, padx=20, pady=20)
computer_label.grid(row=0, column=2, padx=20, pady=20)

def play(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    player_label.config(image=images[player_choice])
    computer_label.config(image=images[computer_choice])

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "Computer wins!"

    tk.messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

btn_rock = tk.Button(root, text="Rock", command=lambda: play('rock'))
btn_paper = tk.Button(root, text="Paper", command=lambda: play('paper'))
btn_scissors = tk.Button(root, text="Scissors", command=lambda: play('scissors'))

btn_rock.grid(row=1, column=0, pady=10)
btn_paper.grid(row=1, column=1, pady=10)
btn_scissors.grid(row=1, column=2, pady=10)

root.mainloop()