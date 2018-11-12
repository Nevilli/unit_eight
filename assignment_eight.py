import tkinter

root = tkinter.Tk()
root.title("Liam's Special Calculator")


def one():
    answer = entry.get()
    entry.set(answer + "1")


def two():
    answer = entry.get()
    entry.set(answer + "2")


def three():
    answer = entry.get()
    entry.set(answer + "3")


def four():
    answer = entry.get()
    entry.set(answer + "4")


def five():
    answer = entry.get()
    entry.set(answer + "5")


def six():
    answer = entry.get()
    entry.set(answer + "6")


def seven():
    answer = entry.get()
    entry.set(answer + "7")


def eight():
    answer = entry.get()
    entry.set(answer + "8")


def nine():
    answer = entry.get()
    entry.set(answer + "9")


def zero():
    answer = entry.get()
    entry.set(answer + "0")


def zero_zero():
    answer = entry.get()
    entry.set(answer + "00")

def division():
    answer = entry.get()
    entry.set(answer )

def one():
    answer = entry.get()
    entry.set(answer + "1")

def one():
    answer = entry.get()
    entry.set(answer + "1")

def one():
    answer = entry.get()
    entry.set(answer + "1")

def one():
    answer = entry.get()
    entry.set(answer + "1")

def one():
    answer = entry.get()
    entry.set(answer + "1")


entry = tkinter.StringVar()

title = tkinter.Label(root, text="Liam's Special Calculator")
title.grid(row=1, column=1, columnspan=5)

main_entry = tkinter.Entry(root, textvariable=entry)
main_entry.grid(row=2, column=1, columnspan=5)

clear = tkinter.Button(root, text="C")
clear.grid(row=3, column=1)

seven = tkinter.Button(root, text="7", command=seven)
seven.grid(row=3, column=2)

eight = tkinter.Button(root, text="8", command=eight)
eight.grid(row=3, column=3)

nine = tkinter.Button(root, text="9", command=nine)
nine.grid(row=3, column=4)

division = tkinter.Button(root, text="/")
division.grid(row=3, column=5)

squared = tkinter.Button(root, text="x2")
squared.grid(row=4, column=1)

four = tkinter.Button(root, text="4", command=four)
four.grid(row=4, column=2)

five = tkinter.Button(root, text="5", command=five)
five.grid(row=4, column=3)

six = tkinter.Button(root, text="6", command=six)
six.grid(row=4, column=4)

times = tkinter.Button(root, text="x")
times.grid(row=4, column=5)

percent = tkinter.Button(root, text="%")
percent.grid(row=5, column=1)

one = tkinter.Button(root, text="1", command=one)
one.grid(row=5, column=2)

two = tkinter.Button(root, text="2", command=two)
two.grid(row=5, column=3)

three = tkinter.Button(root, text="3", command=three)
three.grid(row=5, column=4)

minus = tkinter.Button(root, text="-")
minus.grid(row=5, column=5)

zero_zero = tkinter.Button(root, text="00", command = zero_zero)
zero_zero.grid(row=6, column=1)

zero = tkinter.Button(root, text="0", command= zero)
zero.grid(row=6, column=2)

decimal = tkinter.Button(root, text=".")
decimal.grid(row=6, column=3)

equals = tkinter.Button(root, text="=")
equals.grid(row=6, column=4)

plus = tkinter.Button(root, text="+")
plus.grid(row=6, column=5)

root.mainloop()
