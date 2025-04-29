import tkinter as tk
from tkinter import ttk
import random
import winsound

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x350")
        
        # Center window on screen
        window_width = 300
        window_height = 350
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        bg_color = "#f0f0f0"
        header_font = ("Arial", 16, "bold")
        text_font = ("Arial", 12)
        
        self.secret_number = random.randint(1, 50)  # Changed here
        self.attempts = 0
        
        style = ttk.Style()
        style.configure('TButton', font=text_font)
        style.configure('TLabel', font=text_font, background=bg_color)
        style.configure('TEntry', font=text_font)
        
        self.guess_label = ttk.Label(master, text="Enter your guess (1-50):", font=header_font, background=bg_color)  # Changed here
        self.guess_label.pack(pady=10)
        
        self.guess_entry = ttk.Entry(master, font=text_font)
        self.guess_entry.pack(pady=5, ipady=5, ipadx=5)
        
        self.result_label = ttk.Label(master, text="", font=text_font, background=bg_color)
        self.result_label.pack(pady=5)
        
        self.submit_button = ttk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5, ipady=5, ipadx=10)
        
        self.reset_button = ttk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5, ipady=5, ipadx=10)
        
        self.clue_label = ttk.Label(master, text="", font=text_font, background=bg_color)
        self.clue_label.pack(pady=5)
        
        self.timer_label = ttk.Label(master, text="Time Left: 10", font=text_font, background=bg_color)
        self.timer_label.pack(pady=5)
        self.remaining_time = 10
        self.timer()
        
    def timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}")
            self.master.after(1000, self.timer)
        else:
            self.result_label.config(text="Time's up! You ran out of time.")
            self.submit_button.config(state=tk.DISABLED)
        
    def check_guess(self):
        guess = self.guess_entry.get()
        try:
            guess = int(guess)
            if guess < 1 or guess > 50:  # Changed here
                self.result_label.config(text="Please enter a number between 1 and 50.")
            else:
                self.attempts += 1
                if guess < self.secret_number:
                    self.result_label.config(text="Too low! Try again.")
                    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
                elif guess > self.secret_number:
                    self.result_label.config(text="Too high! Try again.")
                    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
                else:
                    self.result_label.config(text="Congratulations! You guessed it right!")
                    winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
        finally:
            self.update_attempts()
        
    def update_attempts(self):
        self.clue_label.config(text=f"Attempts: {self.attempts}")
        
    def reset_game(self):
        self.secret_number = random.randint(1, 50)  # Changed here
        self.attempts = 0
        self.result_label.config(text="")
        self.clue_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.remaining_time = 20
        self.timer_label.config(text="Time Left: 10")
        self.timer()

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
