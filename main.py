from tkinter import *
import pandas as pd
from random import *
BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------------------DATA EXTRACTION-----------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/afrikaans_words.csv")

afrikaans_words = data["Afrikaans"].to_list()
english_words = data["English"].to_list()
words_to_learn = data.to_dict(orient="records")  # list of dictionaries
print(words_to_learn)
index = 0


def new_afri_word():
    global index, flip_time
    window.after_cancel(flip_time)
    index = randint(0, len(words_to_learn) - 1)
    canvas.itemconfig(canvas_image, image=card_front_img)
    afri_word_label.config(text=afrikaans_words[index], fg="black", bg="white")
    afrikaans_label.config(text="Afrikaans", fg="black", bg="white")
    flip_time = window.after(3000, func=flip_card)  # timer is reset


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    afri_word_label.config(text=english_words[index], fg="white", bg="#91c2af")
    afrikaans_label.config(text="English", fg="white", bg="#91c2af")


def is_known():
    words_to_learn.pop(index)
    print(len(words_to_learn))
    new_data = pd.DataFrame(words_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_afri_word()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_time = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

canvas_image = canvas.create_image(400, 270, image=card_front_img)

canvas.grid(row=0, column=0, columnspan=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_afri_word)
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
wrong_btn.config(borderwidth=0)
right_btn.config(borderwidth=0)

wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

afrikaans_label = Label(text="Afrikaans", font=("Times", 40, "italic"), bg="white")
afrikaans_label.place(x=400, y=150, anchor="center")

afri_word_label = Label(text=afrikaans_words[0], font=("Ariel", 60, "bold"), bg="white")
afri_word_label.place(x=400, y=280, anchor="center")


window.mainloop()
