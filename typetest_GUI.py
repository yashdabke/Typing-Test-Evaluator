import time
import random
import tkinter as tk
from tkinter import messagebox

# Lists of phrases for different difficulty levels
easy_phrases = [
    "The quick brown fox jumps over the lazy dog.",
    "To be or not to be, that is the question!",
    "Beggars can't be choosers, but they can be heroes.",
    "Life is like a box of chocolates.",
    "You can't judge a book by its cover.",
    "All that glitters is not gold.",
    "Better late than never.",
    "Actions speak louder than words.",
    "A picture is worth a thousand words.",
    "Don't count your chickens before they hatch.",
]

medium_phrases = [
    "In the middle of difficulty lies opportunity.",
    "A penny for your thoughts? How about a dollar for your dreams?",
    "Honesty is the best policy, but insanity is a better defense.",
    "Where there's a will, there's a way.",
    "Don't cry over spilled milk.",
    "Every cloud has a silver lining, but sometimes you need an umbrella.",
    "When in Rome, do as the Romans do.",
    "The pen is mightier than the sword.",
    "Laughter is the best medicine.",
    "A stitch in time saves nine.",
]

hard_phrases = [
    "Coding is the language of the future, and the future is now!",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "When the going gets tough, the tough get going.",
    "Fortune favors the bold.",
    "The only way to do great work is to love what you do.",
    "Opportunity does not knock, it presents itself when you beat down the door.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "The harder I work, the luckier I get.",
    "The best way to predict the future is to create it.",
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.difficulty_level = tk.StringVar()
        self.difficulty_level.set("easy")

        self.phrase_label = tk.Label(root, text="", font=("Arial", 14))
        self.phrase_label.pack(pady=20)

        self.user_input_entry = tk.Entry(root, font=("Arial", 14))
        self.user_input_entry.pack(pady=10)
        self.user_input_entry.bind("<Return>", self.check_input)  # Bind Enter key to check_input

        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test, font=("Arial", 14))
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, font=("Arial", 14))
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state=tk.DISABLED)

        self.create_difficulty_radio_buttons()

        # Track whether the typing window is cleared or not
        self.is_typing_window_cleared = False

    def create_difficulty_radio_buttons(self):
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack(pady=10)

        tk.Label(difficulty_frame, text="Select Difficulty Level:", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

        easy_radio = tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty_level, value="easy")
        easy_radio.pack(side=tk.LEFT)
        easy_radio.select()

        medium_radio = tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty_level, value="medium")
        medium_radio.pack(side=tk.LEFT)

        hard_radio = tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty_level, value="hard")
        hard_radio.pack(side=tk.LEFT)

    def start_typing_test(self):
        self.clear_typing_window()  # Clear the typing window
        self.start_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.DISABLED)

        difficulty = self.difficulty_level.get()
        self.current_phrase = self.select_phrase(difficulty)

        self.phrase_label.config(text=self.current_phrase)
        self.user_input_entry.config(state=tk.NORMAL)
        self.user_input_entry.focus()
        self.start_time = time.time()
        self.total_words_typed = 0

    def select_phrase(self, difficulty_level):
        if difficulty_level == 'easy':
            return random.choice(easy_phrases)
        elif difficulty_level == 'medium':
            return random.choice(medium_phrases)
        elif difficulty_level == 'hard':
            return random.choice(hard_phrases)
        else:
            return random.choice(easy_phrases)

    def check_input(self, event):
        user_input = self.user_input_entry.get()
        end_time = time.time()

        input_words = user_input.split()
        correct_words = [w for w in input_words if w.strip('.,?!') in self.current_phrase.strip('.,?!')]

        accuracy = len(correct_words) / len(input_words) if input_words else 0
        time_taken = end_time - self.start_time

        self.total_words_typed += len(input_words)

        result_text = f"Accuracy: {round(accuracy * 100, 2)}%, Time Taken: {round(time_taken, 2)} seconds, Total Words Typed: {self.total_words_typed}"
        self.result_label.config(text=result_text)
        self.result_label.pack(pady=20)

        if accuracy > 0.8:
            self.play_again_button.config(state=tk.NORMAL)

        self.user_input_entry.config(state=tk.DISABLED)

    def play_again(self):
        self.clear_typing_window()  # Clear the typing window
        self.start_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.result_label.config(text="")
        self.user_input_entry.config(state=tk.NORMAL)
        self.user_input_entry.focus()
        self.current_phrase = ""

    def clear_typing_window(self):
        if not self.is_typing_window_cleared:
            self.user_input_entry.delete(0, tk.END)
            self.is_typing_window_cleared = True

def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
