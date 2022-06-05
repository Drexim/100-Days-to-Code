import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


# Function to generate new word.
def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_card, image=card_front_img)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_card, image=card_back_img)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")


def correct_guess():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data\words_to_learn.csv", index=False)
    new_word()


# Window
window = tk.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Images
card_front_img = tk.PhotoImage(file=".\images\card_front.png")
card_back_img = tk.PhotoImage(file=".\images\card_back.png")
right_img = tk.PhotoImage(file=r".\images\right.png")
wrong_img = tk.PhotoImage(file=".\images\wrong.png")

# Data to dictionary - to_learn[num] to pick the French word and English word.
try:
    data = pd.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"data\french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Card Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Text
language_label = canvas.create_text(400, 150, text="", font=("Arial", 30, "italic"), anchor="center")
word_label = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold",), anchor="center")

# Buttons
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = tk.Button(image=right_img, highlightthickness=0, command=correct_guess)
right_button.grid(column=1, row=1)

new_word()

window.mainloop()
