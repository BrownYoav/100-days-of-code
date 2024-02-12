from tkinter import *

def convertion():
    km_value = int(entry_input.get()) *1.6
    km_value = round(km_value,1)

    value_label["text"] = km_value


window = Tk()
window.title
window.minsize(width=300, height=200)

#Entry
entry_input = Entry()
entry_input.config(width=10)
entry_input.grid(row=0,column=1)

#miles label
miles_label = Label(text='Miles')
miles_label.grid(row=0,column=2)

#prompt label
prompt_label= Label(text='Is equal to ')
prompt_label.grid(row=1,column=0)

#value label
value_label = Label(text='0')
value_label.grid(row=1,column=1)

# km label
km_label = Label(text='Km')
km_label.grid(row=1,column=2)

# calculate Button
calculate_button = Button(text="calculate", command=convertion)
calculate_button.grid(row=2,column=1)


window.mainloop()