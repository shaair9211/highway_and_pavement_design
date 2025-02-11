import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk




root = tk.Tk()
root.withdraw()
# result = messagebox.showinfo("Welcome!", f"IN THIS PROGRAM WE ARE GOING TO CALCULATE THE THICKNESS OF FLEXIBLE PAVEMENT")


# class DualInputDialog(simpledialog.Dialog):
#     def body(self, master):
#         tk.Label(master, text="Enter value for initial servicibility").grid(row=0)
#         tk.Label(master, text="Enter value for terminal servicibility").grid(row=1)

#         self.var1_entry = tk.Entry(master)
#         self.var2_entry = tk.Entry(master)

#         self.var1_entry.grid(row=0, column=1)
#         self.var2_entry.grid(row=1, column=1)
#         return self.var1_entry
#     def apply(self):
#         self.var1 = self.var1_entry.get()
#         self.var2 = self.var2_entry.get()

# def ask_for_values():
#     root = tk.Tk()
#     root.withdraw()
#     dialog = DualInputDialog(root)
#     var1 = dialog.var1
#     var2 = dialog.var2
#     if var1 and var2:
#         print(f"User entered values: Initial Serviceability = {var1}, Terminal Serviceability = {var2}")
#         return var1, var2
#     else:
#         print("User cancelled the input")

# Po, Pt = ask_for_values()
# Po, Pt = float(Po), float(Pt)
# PSI = Po - Pt
# print(PSI)


def show_image_and_input():
    image_path = r'Highway and Pavement\resources\reliability.png'  # Corrected path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    top = tk.Toplevel()
    top.title("Insert Reliability")

    text_label = tk.Label(top, text="Insert the value of reliability")
    text_label.pack()

    label = tk.Label(top, image=photo)
    label.image = photo
    label.pack()

    # Input section
    input_label = tk.Label(top, text="Enter a value in Percentage:")
    input_label.pack()
    input_entry = tk.Entry(top)
    input_entry.pack()

    def on_submit():
        global R  # Declare R as global inside the function
        R = input_entry.get()
        if R:
            print(f"User entered value of reliability: {R}")
        top.destroy()

    submit_button = tk.Button(top, text="Submit", command=on_submit)
    submit_button.pack()

root = tk.Tk()
root.withdraw()
R = None
show_image_and_input()
root.mainloop()
print(f"The value of R is: {R}")



def show_image_and_input():
    image_path_2 = r'Highway and Pavement\resources\standard_deviation.png'
    image = Image.open(image_path_2)
    photo = ImageTk.PhotoImage(image)

    top = tk.Toplevel()
    top.title("Insert Standard Deviation")

    text_label = tk.Label(top, text="Insert the value of Standard Deviation")
    text_label.pack()

    label = tk.Label(top, image=photo)
    label.image = photo
    label.pack()

    # Input section
    input_label = tk.Label(top, text="Enter a value in Percentage:")
    input_label.pack()
    input_entry = tk.Entry(top)
    input_entry.pack()

    def on_submit():
        global So
        So = input_entry.get()
        if So:
            print(f"User entered value of Standard Deviation: {So}")
        top.destroy()

    submit_button = tk.Button(top, text="Submit", command=on_submit)
    submit_button.pack()

# root = tk.Tk()
# root.withdraw()
So = None
show_image_and_input()
print(f"The value of So is: {So}")


def ESAL():
    root = tk.Tk()
    root.withdraw()
    ESAL = simpledialog.askstring("Input", "Enter the value of ESAL:")

    if ESAL:
        print(f"User entered value of ESAL: {ESAL}")
    else:
        print("User cancelled the input")

























root.mainloop()
