from tkinter import *
import pandas
import random
import shutil

BACKGROUND_COLOR = "#B1DDC6"

random_word = {}
# -------------------------------------- FUNCTIONS --------------------------------------

def generate_random_word():
    global random_word
    random_word = random.choice(words_to_learn)
    french_word = random_word["French"]
    canvas.itemconfig(card_language,text="French",fill="black")
    canvas.itemconfig(card_word, text=french_word,fill="black")
    canvas.itemconfig(canvas_image,image=front_card_image)

def flip_card():
    english_word = random_word["English"]

    canvas.itemconfig(card_language,text='English',fill="white")
    canvas.itemconfig(card_word,text=english_word,fill="white")
    canvas.itemconfig(canvas_image,image=back_card_image)

def known_word():

    words_to_learn.remove(random_word)
    print(len(words_to_learn))
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)


    generate_random_word()



# -------------------------------------- APP LOGIC --------------------------------------
# Create data
try:
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    shutil.copyfile("data/french_words.csv","data/words_to_learn.csv")
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
finally:
    words_to_learn = words_to_learn.to_dict(orient='records')



# -------------------------------------- UI SET UP --------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#canvas
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0,column=0,columnspan=3)

card_language = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))


#Butons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=2)

translate_image = Button(height=5, width=30, text="Translate", font=("Ariel", 20), command=flip_card)
translate_image.grid(row=1, column=1)




generate_random_word()


window.mainloop()