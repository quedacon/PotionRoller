from tkinter import *

import potion_roller
import quip
import html_maker


def make_potion_list():
    number = int(number_entry.get())
    potion_list = potion_roller.generate_potions(number)
   # fake_list = ["im a potion", "me too", "yeah me three"]
    #html_maker.make_list_page(fake_list)
    html_maker.make_list_page(potion_list)


root = Tk()
root.geometry = ("500x500")

top = Frame(root)
top.pack()
frame = Frame(root)
frame.pack()
bottom = Frame(root)
bottom.pack()

main_label = Label(
    top,
    font = ("Arial", 14),
    text = "Potion Roller!",
)
main_label.pack(side = TOP)

sublabel = Label(
    top,
    font = ("Arial", 9),
    text = quip.random_string(),
)
sublabel.pack(side = BOTTOM)

number_entry = Entry(
    frame
)
number_entry.insert(0, "1")
number_entry.pack(side = LEFT)

generate_button = Button(
    frame,
    text = "Generate Potions",
    command = make_potion_list
)
generate_button.pack(side = RIGHT)

root.title("Potion Roller")
root.mainloop()
