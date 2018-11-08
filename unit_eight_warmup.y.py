import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")

f_value = tkinter.StringVar()
c_value = tkinter.StringVar()

f_label = tkinter.Label(root, text="Degrees Fahrenheit")
f_label.grid(row=1, column=1)

f_label_entry = tkinter.Entry(root, textvariable=f_value)
f_label_entry.grid(row=1, column=2)

C_label = tkinter.Label(root, text="Degrees Celsius")
C_label.grid(row=2, column=1)

C_label_entry = tkinter.Label(root, textvariable=c_value)
C_label_entry.grid(row=2, column=2)

root.mainloop()
