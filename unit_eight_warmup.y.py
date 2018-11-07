import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

f_label = tkinter.Label(root, text="Degrees Fahrenheit")
f_label.grid(row=1, column=1)

f_label_entry = tkinter.Entry(root)
f_label_entry.grid(row=1, column=2)

C_label = tkinter.Label(root, text="Degrees Celsius")
C_label.grid(row=2, column=1)

C_label_entry = tkinter.Entry(root)
C_label_entry.grid(row=2, column=2)
root.mainloop()