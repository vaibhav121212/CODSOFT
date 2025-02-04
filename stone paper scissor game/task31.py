import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        

        
        self.user_score = 0
        self.computer_score = 0

        
        self.title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("arial", 24,"bold"))
        self.title_label.pack(pady=30)

        
        self.score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("comic sans", 19))
        self.score_label.pack(pady=10)

        
        self.rock_button = tk.Button(root, text="Rock", width=25, height=3, command=lambda: self.play("rock"))
        self.rock_button.pack(pady=10)

        self.paper_button = tk.Button(root, text="Paper", width=25, height=3, command=lambda: self.play("paper"))
        self.paper_button.pack(pady=10)
        

        self.scissors_button = tk.Button(root, text="Scissors", width=25, height=3, command=lambda: self.play("scissors"))
        self.scissors_button.pack(pady=10)

        
        self.result_label = tk.Label(root, text="Make your choice!", font=("Helvetica", 14))
        self.result_label.pack(pady=30)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def update_score(self, winner):
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)

        
        self.result_label.config(text=f"You chose {user_choice.capitalize()}\nComputer chose {computer_choice.capitalize()}\n")

        if winner == 'user':
            self.result_label.config(text=f"{self.result_label['text']}You win this round!")
        elif winner == 'computer':
            self.result_label.config(text=f"{self.result_label['text']}Computer wins this round!")
        else:
            self.result_label.config(text=f"{self.result_label['text']}It's a tie!")

        
        self.update_score(winner)

        
        play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if not play_again:
            self.root.quit()


root = tk.Tk()


app = RockPaperScissorsApp(root)


root.mainloop()
