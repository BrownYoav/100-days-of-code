from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    pyperclip.copy(password)
    password_entry.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(username)==0 or len(password)== 0:
        messagebox.showerror(title='Error', message='One of the fields was not filled properly')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details you have entered: \nEmail/username: {username}'
                                                          f'\nPassword: {password} \nIs that right?')
        if is_ok :
            with open('data.txt',"a") as file:
                file.write(f'{website} | {username} | {password}\n')

        #clearing fields
            website_entry.delete(0,'end')
            username_entry.delete(0,'end')
            password_entry.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50,padx=50)

canvas = Canvas(highlightthickness=0,width=200,height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)

username_entry = Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(row=3,column=1)

# labels
website_label = Label(text='Website: ')
website_label.grid(row=1,column=0)

username_label = Label(text='Email/Username: ')
username_label.grid(row=2,column=0)

password_label = Label(text='Password: ')
password_label.grid(row=3,column=0)

#buttons
generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(row=3,column=2)

add_button = Button(width=34, text='Add', command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()


