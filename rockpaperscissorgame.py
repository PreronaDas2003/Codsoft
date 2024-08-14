import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.computer_score = 0
        self.user_score = 0

        self.start_label = tk.Label(self.window, text="Welcome to Rock Paper Scissors!")
        self.start_label.pack()

        self.start_button = tk.Button(self.window, text="Start", command=self.start_game)
        self.start_button.pack()

        self.window.mainloop()

    def start_game(self):
        self.start_label.destroy()
        self.start_button.destroy()

        self.choice_label = tk.Label(self.window, text="Choose your move:")
        self.choice_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack()

       # self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
       # self.quit_button.pack()

        self.score_label = tk.Label(self.window, text="Score: You - 0, Computer - 0")
        self.score_label.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        self.result_label.config(text=f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            self.result_label.config(text=self.result_label.cget("text") + "\nIt's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.result_label.config(text=self.result_label.cget("text") + "\nYou win!")
            self.user_score += 1
        else:
            self.result_label.config(text=self.result_label.cget("text") + "\nComputer wins!")
            self.computer_score += 1

        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

        self.play_again_label = tk.Label(self.window, text="Do you want to play again?")
        self.play_again_label.pack()

        self.yes_button = tk.Button(self.window, text="Yes", command=self.reset_game)
        self.yes_button.pack()

        self.no_button = tk.Button(self.window, text="No", command=self.window.destroy)
        self.no_button.pack()

    def reset_game(self):
        self.result_label.config(text="")
        self.play_again_label.destroy()
        self.yes_button.destroy()
        self.no_button.destroy()

if __name__ == "__main__":
    game = RockPaperScissors()