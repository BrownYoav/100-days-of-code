from tkinter import *

def button_clicked():
    my_label["text"] = my_entry.get()
    # my_label.config(text='i was clicked')

#window
window = Tk()
window.minsize(width=500, height=500)

# label
my_label = Label(text='hello', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# button 1
button1 = Button(text='click me', command=button_clicked)
button1.grid(column=1, row=1)

# button 2
button1 = Button(text='new button', command=button_clicked)
button1.grid(column=2, row=0)

# entry
my_entry = Entry()
my_entry.grid(column=3, row=3 )






window.mainloop()
