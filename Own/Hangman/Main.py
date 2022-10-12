from Game import Hangman
from backend import word_generator
from tkinter import *

h = Hangman(word_generator())

root = Tk()
root.title("Hangman")

welcome_promp = Label(root, text="Hangman", width=100)
welcome_promp.grid(row=0, column=0, columnspan=3)


root.mainloop()

h = Hangman(word_generator())
print(h.game())