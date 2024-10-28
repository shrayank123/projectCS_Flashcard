#importing modules
from tkinter import *
from pandas import *
import random

#constant value to set background color
BACKGROUND_COLOR = "#B1DDC6"

# setting the class Tk() in variable window, then proceeds to make a title
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
try:
    data = read_csv("data/words_not_known.csv")
except FileNotFoundError:
    original_file = read_csv("data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# print(to_learn[2]['French'])
   
def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvasImage, image=cardFront)
    timer = window.after(3000, func=show_answer)


def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("data/words_not_know.csv",index=False)
    next_card()


def show_answer():
    canvas.itemconfig(canvasImage, image=cardBack)
    canvas.itemconfig(language, text="English", fill="white")
    # Find the key for the target value
    canvas.itemconfig(word, text=current_card["English"], fill="white")


timer = window.after(3000, func=show_answer)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")

canvasImage = canvas.create_image(400, 263, image=cardFront)
canvas.grid(row=1, column=0, columnspan=2)

language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# making buttons
tick = PhotoImage(file="images/right.png")
tick_button = Button(image=tick, highlightthickness=0, command=is_known)
tick_button.grid(row=2, column=1)

x = PhotoImage(file="images/wrong.png")
x_button = Button(image=x, highlightthickness=0, command= next_card)
x_button.grid(row=2, column=0)

next_card()
window.mainloop()
