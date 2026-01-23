from tkinter import *
import requests
import pandas
import random



def get_quote():
    word_file = pandas.read_csv(f"AravindQuotes.csv")
    word_dictionary = word_file.to_dict(orient="records")
    current_quote = random.choice(word_dictionary)
    canvas.itemconfig(quote_text, text=current_quote)


window = Tk()
window.title("Aravind Found Quotes...")
window.config(padx=20, pady=20)

canvas = Canvas(width=400, height=514)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Click on Aravind below, and he will give you a famous quote of his!",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Aravind2.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()