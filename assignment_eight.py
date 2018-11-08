import tkinter

root = tkinter.Tk()
root.title("Liam's Special Calculator")

entry = tkinter.StringVar()

title = tkinter.Label(root, text="Liam's Special Calculator")
title.grid(row=1, column=2)

main_entry = tkinter.Entry(root)
main_entry.grid(row=2, column=2)

clear = tkinter.Button(root, text="C")
clear.grid(row=3, column=1)

seven = tkinter.Button(root, text="7")
seven.grid(row=3, column=2)

eight = tkinter.Button(root, text="8")
eight.grid(row=3, column=3)

nine = tkinter.Button(root, text="9")
nine.grid(row=3, column=4)

division = tkinter.Button(root, text="/")
division.grid(row=3, column=5)

squared = tkinter.Button(root, text="x2")
squared.grid(row=4, column=1)

four = tkinter.Button(root, text="4")
four.grid(row=4, column=2)

five = tkinter.Button(root, text="5")
five.grid(row=4, column=3)

six = tkinter.Button(root, text="6")
six.grid(row=4, column=4)

times = tkinter.Button(root, text="x")
times.grid(row=4, column=5)

percent = tkinter.Button(root, text="%")
percent.grid(row=5, column=1)

one = tkinter.Button(root, text="1")
one.grid(row=5, column=2)

two = tkinter.Button(root, text="2")
two.grid(row=5, column=3)

three = tkinter.Button(root, text="3")
three.grid(row=5, column=4)

minus = tkinter.Button(root, text="-")
minus.grid(row=5, column=5)

zero_zero = tkinter.Button(root, text="00")
zero_zero.grid(row=6, column=1)

zero = tkinter.Button(root, text="0")
zero.grid(row=6, column=2)

decimal = tkinter.Button(root, text=".")
decimal.grid(row=6, column=3)

equals = tkinter.Button(root, text="=")
equals.grid(row=6, column=4)

plus = tkinter.Button(root, text="+")
plus.grid(row=6, column=5)

root.mainloop()
