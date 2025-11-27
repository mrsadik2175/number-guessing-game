import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")
        master.geometry("400x200")

        self.number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1-100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.button = tk.Button(master, text="Submit", command=self.check_guess)
        self.button.pack(pady=5)

        self.feedback = tk.Label(master, text="")
        self.feedback.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return

        self.attempts += 1

        if guess < self.number:
            self.feedback.config(text="Too low! Try again.")
        elif guess > self.number:
            self.feedback.config(text="Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()