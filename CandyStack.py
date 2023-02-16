import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import time
# ____________________________________________________________________________________________


class Candy(tk.Tk):
    lst = []

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("CandyDispenser")
        self.geometry('480x640')
        self.configure(bg="seagreen1")

        self.canvas = tk.Canvas(
            self, width=250, height=400, background="lightcyan1", state="normal")
        self.canvas.pack()
        self.canvas.place(x=20, y=200)
# _________________________________________________________________________________________________
        self.canvas.create_line(0, 400, 250, 350, width=3)
        self.canvas.create_line(250, 350, 0, 300, width=3)
        self.canvas.create_line(0, 300, 250, 250, width=3)
        self.canvas.create_line(250, 250, 0, 200, width=3)
        self.canvas.create_line(0, 200, 250, 150, width=3)
        self.canvas.create_line(250, 150, 0, 100, width=3)
        self.canvas.create_line(0, 100, 250, 50, width=3)
        self.canvas.create_line(250, 50, 0, 50, width=3)
# ________________________________________________________________________________________________
        # Buttons:
        self.put_elements = tk.Button(
            self, text="Push", command=self.push).place(relx=.8, rely=.5)

        self.remove_elements = tk.Button(
            self, text="Pop", command=self.pop).place(relx=.8, rely=.6)

        self.is_empty = tk.Button(
            self, text="isEmpty?", command=self.isEmpty).place(relx=.8, rely=.7)

        self.stackSize = tk.Button(
            self, text="Size", command=self.size).place(relx=.8, rely=.8)

        self.tops = tk.Button(
            self, text="Top", command=self.top).place(relx=.8, rely=.9)

# _______________________________________________________________________________________________

    def push(self):

        if len(self.lst) == 0:
            self.lst.append("Blue Candy")
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 300, width=3)
            self.canvas.create_line(0, 300, 250, 250, width=3)
            self.canvas.create_line(250, 250, 0, 200, width=3)
            self.canvas.create_line(0, 200, 250, 150, width=3)
            self.canvas.create_line(250, 150, 0, 100, width=3)
            self.canvas.create_line(0, 100, 250, 50, width=3)
            self.canvas.create_line(250, 50, 0, 50, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="blue")

        elif len(self.lst) == 1:
            self.lst.append("Red Candy")
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 360, width=3)
            self.canvas.create_line(250, 360, 0, 320, width=3)
            self.canvas.create_line(0, 320, 250, 280, width=3)
            self.canvas.create_line(250, 280, 0, 240, width=4)
            self.canvas.create_line(0, 240, 250, 200, width=3)
            self.canvas.create_line(250, 200, 0, 160, width=3)
            self.canvas.create_line(0, 160, 250, 120, width=3)
            self.canvas.create_line(250, 120, 0, 120, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="red")
            self.canvas.create_oval(0, 50, 250, 120, fill="blue")

        elif len(self.lst) == 2:
            self.lst.append("Green Candy")
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 365, width=3)
            self.canvas.create_line(250, 365, 0, 330, width=3)
            self.canvas.create_line(0, 330, 250, 295, width=3)
            self.canvas.create_line(250, 295, 0, 260, width=3)
            self.canvas.create_line(0, 260, 250, 225, width=3)
            self.canvas.create_line(250, 225, 0, 190, width=3)
            self.canvas.create_line(0, 190, 250, 155, width=3)
            self.canvas.create_line(250, 155, 0, 155, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="green")
            self.canvas.create_oval(0, 50, 250, 120, fill="red")
            self.canvas.create_oval(0, 100, 250, 155, fill="blue")

        elif len(self.lst) == 3:
            self.lst.append("Magenta Candy")
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 370, width=3)
            self.canvas.create_line(250, 370, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 310, width=3)
            self.canvas.create_line(250, 310, 0, 280, width=3)
            self.canvas.create_line(0, 280, 250, 250, width=3)
            self.canvas.create_line(250, 250, 0, 220, width=3)
            self.canvas.create_line(0, 220, 250, 190, width=3)
            self.canvas.create_line(250, 190, 0, 190, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="magenta")
            self.canvas.create_oval(0, 50, 250, 120, fill="green")
            self.canvas.create_oval(0, 100, 250, 155, fill="red")
            self.canvas.create_oval(0, 150, 250, 190, fill="blue")

        elif len(self.lst) == 4:
            self.lst.append("Orange Candy")
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 375, width=3)
            self.canvas.create_line(250, 375, 0, 350, width=3)
            self.canvas.create_line(0, 350, 250, 325, width=3)
            self.canvas.create_line(250, 325, 0, 300, width=3)
            self.canvas.create_line(0, 300, 250, 275, width=3)
            self.canvas.create_line(250, 275, 0, 250, width=3)
            self.canvas.create_line(0, 250, 250, 225, width=3)
            self.canvas.create_line(250, 225, 0, 225, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="orange1")
            self.canvas.create_oval(0, 50, 250, 120, fill="magenta")
            self.canvas.create_oval(0, 100, 250, 155, fill="green")
            self.canvas.create_oval(0, 150, 250, 190, fill="red")
            self.canvas.create_oval(0, 190, 250, 230, fill="blue")

        elif len(self.lst) == 5:
            del self.canvas
            self.lst.append("Black Candy")
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 380, width=3)
            self.canvas.create_line(250, 380, 0, 360, width=3)
            self.canvas.create_line(0, 360, 250, 340, width=3)
            self.canvas.create_line(250, 340, 0, 320, width=3)
            self.canvas.create_line(0, 320, 250, 300, width=3)
            self.canvas.create_line(250, 300, 0, 280, width=3)
            self.canvas.create_line(0, 280, 250, 260, width=3)
            self.canvas.create_line(250, 260, 0, 260, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="black")
            self.canvas.create_oval(0, 50, 250, 120, fill="orange")
            self.canvas.create_oval(0, 100, 250, 155, fill="magenta")
            self.canvas.create_oval(0, 150, 250, 190, fill="green")
            self.canvas.create_oval(0, 190, 250, 230, fill="red")
            self.canvas.create_oval(0, 230, 250, 260, fill="blue")

        elif len(self.lst) == 6:
            del self.canvas
            self.lst.append("Gray Candy")
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 385, width=3)
            self.canvas.create_line(250, 385, 0, 370, width=3)
            self.canvas.create_line(0, 370, 250, 355, width=3)
            self.canvas.create_line(250, 355, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 325, width=3)
            self.canvas.create_line(250, 325, 0, 310, width=3)
            self.canvas.create_line(0, 310, 250, 295, width=3)
            self.canvas.create_line(250, 295, 0, 295, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="gray37")
            self.canvas.create_oval(0, 50, 250, 120, fill="black")
            self.canvas.create_oval(0, 100, 250, 155, fill="orange")
            self.canvas.create_oval(0, 150, 250, 190, fill="magenta")
            self.canvas.create_oval(0, 190, 250, 230, fill="green")
            self.canvas.create_oval(0, 230, 250, 260, fill="red")
            self.canvas.create_oval(0, 260, 250, 295, fill="blue")

        elif len(self.lst) == 7:
            del self.canvas
            self.lst.append("Beige Candy")
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 390, width=3)
            self.canvas.create_line(250, 390, 0, 380, width=3)
            self.canvas.create_line(0, 380, 250, 370, width=3)
            self.canvas.create_line(250, 370, 0, 360, width=3)
            self.canvas.create_line(0, 360, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 330, width=3)
            self.canvas.create_line(250, 330, 0, 330, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="bisque")
            self.canvas.create_oval(0, 50, 250, 120, fill="gray37")
            self.canvas.create_oval(0, 100, 250, 155, fill="black")
            self.canvas.create_oval(0, 150, 250, 190, fill="orange")
            self.canvas.create_oval(0, 190, 250, 230, fill="magenta")
            self.canvas.create_oval(0, 230, 250, 260, fill="green")
            self.canvas.create_oval(0, 260, 250, 295, fill="red")
            self.canvas.create_oval(0, 295, 250, 330, fill="blue")

        elif len(self.lst) > 7:
            self.canvas.create_line(0, 400, 250, 390, width=3)
            self.canvas.create_line(250, 390, 0, 380, width=3)
            self.canvas.create_line(0, 380, 250, 370, width=3)
            self.canvas.create_line(250, 370, 0, 360, width=3)
            self.canvas.create_line(0, 360, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 330, width=3)
            self.canvas.create_line(250, 330, 0, 330, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="bisque")
            self.canvas.create_oval(0, 50, 250, 120, fill="gray37")
            self.canvas.create_oval(0, 100, 250, 155, fill="black")
            self.canvas.create_oval(0, 150, 250, 190, fill="orange")
            self.canvas.create_oval(0, 190, 250, 230, fill="magenta")
            self.canvas.create_oval(0, 230, 250, 260, fill="green")
            self.canvas.create_oval(0, 260, 250, 295, fill="red")
            self.canvas.create_oval(0, 295, 250, 330, fill="blue")

            showerror(title="CandyDispenser",
                      message="Candy dispenser is full")
# ______________________________________________________________________________________________

    def pop(self):
        if len(self.lst) == 1:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 300, width=3)
            self.canvas.create_line(0, 300, 250, 250, width=3)
            self.canvas.create_line(250, 250, 0, 200, width=3)
            self.canvas.create_line(0, 200, 250, 150, width=3)
            self.canvas.create_line(250, 150, 0, 100, width=3)
            self.canvas.create_line(0, 100, 250, 50, width=3)
            self.canvas.create_line(250, 50, 0, 50, width=3)

        elif len(self.lst) == 2:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 300, width=3)
            self.canvas.create_line(0, 300, 250, 250, width=3)
            self.canvas.create_line(250, 250, 0, 200, width=3)
            self.canvas.create_line(0, 200, 250, 150, width=3)
            self.canvas.create_line(250, 150, 0, 100, width=3)
            self.canvas.create_line(0, 100, 250, 50, width=3)
            self.canvas.create_line(250, 50, 0, 50, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="blue")

        elif len(self.lst) == 3:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 360, width=3)
            self.canvas.create_line(250, 360, 0, 320, width=3)
            self.canvas.create_line(0, 320, 250, 280, width=3)
            self.canvas.create_line(250, 280, 0, 240, width=4)
            self.canvas.create_line(0, 240, 250, 200, width=3)
            self.canvas.create_line(250, 200, 0, 160, width=3)
            self.canvas.create_line(0, 160, 250, 120, width=3)
            self.canvas.create_line(250, 120, 0, 120, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="red")
            self.canvas.create_oval(0, 50, 250, 120, fill="blue")

        elif len(self.lst) == 4:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 365, width=3)
            self.canvas.create_line(250, 365, 0, 330, width=3)
            self.canvas.create_line(0, 330, 250, 295, width=3)
            self.canvas.create_line(250, 295, 0, 260, width=3)
            self.canvas.create_line(0, 260, 250, 225, width=3)
            self.canvas.create_line(250, 225, 0, 190, width=3)
            self.canvas.create_line(0, 190, 250, 155, width=3)
            self.canvas.create_line(250, 155, 0, 155, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="green")
            self.canvas.create_oval(0, 50, 250, 120, fill="red")
            self.canvas.create_oval(0, 100, 250, 155, fill="blue")

        elif len(self.lst) == 5:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 370, width=3)
            self.canvas.create_line(250, 370, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 310, width=3)
            self.canvas.create_line(250, 310, 0, 280, width=3)
            self.canvas.create_line(0, 280, 250, 250, width=3)
            self.canvas.create_line(250, 250, 0, 220, width=3)
            self.canvas.create_line(0, 220, 250, 190, width=3)
            self.canvas.create_line(250, 190, 0, 190, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="magenta")
            self.canvas.create_oval(0, 50, 250, 120, fill="green")
            self.canvas.create_oval(0, 100, 250, 155, fill="red")
            self.canvas.create_oval(0, 150, 250, 190, fill="blue")

        elif len(self.lst) == 6:
            self.lst.pop()
            del self.canvas
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 375, width=3)
            self.canvas.create_line(250, 375, 0, 350, width=3)
            self.canvas.create_line(0, 350, 250, 325, width=3)
            self.canvas.create_line(250, 325, 0, 300, width=3)
            self.canvas.create_line(0, 300, 250, 275, width=3)
            self.canvas.create_line(250, 275, 0, 250, width=3)
            self.canvas.create_line(0, 250, 250, 225, width=3)
            self.canvas.create_line(250, 225, 0, 225, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="orange1")
            self.canvas.create_oval(0, 50, 250, 120, fill="magenta")
            self.canvas.create_oval(0, 100, 250, 155, fill="green")
            self.canvas.create_oval(0, 150, 250, 190, fill="red")
            self.canvas.create_oval(0, 190, 250, 230, fill="blue")

        elif len(self.lst) == 7:
            del self.canvas
            self.lst.pop()
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 380, width=3)
            self.canvas.create_line(250, 380, 0, 360, width=3)
            self.canvas.create_line(0, 360, 250, 340, width=3)
            self.canvas.create_line(250, 340, 0, 320, width=3)
            self.canvas.create_line(0, 320, 250, 300, width=3)
            self.canvas.create_line(250, 300, 0, 280, width=3)
            self.canvas.create_line(0, 280, 250, 260, width=3)
            self.canvas.create_line(250, 260, 0, 260, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="black")
            self.canvas.create_oval(0, 50, 250, 120, fill="orange")
            self.canvas.create_oval(0, 100, 250, 155, fill="magenta")
            self.canvas.create_oval(0, 150, 250, 190, fill="green")
            self.canvas.create_oval(0, 190, 250, 230, fill="red")
            self.canvas.create_oval(0, 230, 250, 260, fill="blue")

        elif len(self.lst) == 8:
            del self.canvas
            self.lst.pop()
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 385, width=3)
            self.canvas.create_line(250, 385, 0, 370, width=3)
            self.canvas.create_line(0, 370, 250, 355, width=3)
            self.canvas.create_line(250, 355, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 325, width=3)
            self.canvas.create_line(250, 325, 0, 310, width=3)
            self.canvas.create_line(0, 310, 250, 295, width=3)
            self.canvas.create_line(250, 295, 0, 295, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="gray37")
            self.canvas.create_oval(0, 50, 250, 120, fill="black")
            self.canvas.create_oval(0, 100, 250, 155, fill="orange")
            self.canvas.create_oval(0, 150, 250, 190, fill="magenta")
            self.canvas.create_oval(0, 190, 250, 230, fill="green")
            self.canvas.create_oval(0, 230, 250, 260, fill="red")
            self.canvas.create_oval(0, 260, 250, 295, fill="blue")

        elif len(self.lst) == 9:
            del self.canvas
            self.lst.pop()
            self.canvas = tk.Canvas(
                self, width=250, height=400, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=20, y=200)
            self.canvas.create_line(0, 400, 250, 390, width=3)
            self.canvas.create_line(250, 390, 0, 380, width=3)
            self.canvas.create_line(0, 380, 250, 370, width=3)
            self.canvas.create_line(250, 370, 0, 360, width=3)
            self.canvas.create_line(0, 360, 250, 350, width=3)
            self.canvas.create_line(250, 350, 0, 340, width=3)
            self.canvas.create_line(0, 340, 250, 330, width=3)
            self.canvas.create_line(250, 330, 0, 330, width=3)
            self.canvas.create_oval(0, 0, 250, 50, fill="bisque")
            self.canvas.create_oval(0, 50, 250, 120, fill="gray37")
            self.canvas.create_oval(0, 100, 250, 155, fill="black")
            self.canvas.create_oval(0, 150, 250, 190, fill="orange")
            self.canvas.create_oval(0, 190, 250, 230, fill="magenta")
            self.canvas.create_oval(0, 230, 250, 260, fill="green")
            self.canvas.create_oval(0, 260, 250, 295, fill="red")
            self.canvas.create_oval(0, 295, 250, 330, fill="blue")


# ________________________________________________________________________________________________

    def isEmpty(self):
        if len(self.lst) == 0:
            print("True")
            showinfo(title="isEmpty?", message="True")
            return True

        else:
            showinfo(title="Is Empty", message="False")
# __________________________________________________________________________________________________

    def size(self):
        self.Size = len(self.lst)
        showinfo(title="Size", message=f"{self.Size}")
        print(self.Size)
        return self.Size
# _________________________________________________________________________________________________

    def top(self):
        if len(self.lst) == 0:
            showinfo(title="Top Candy", message=f"No top Candy")
        else:
            self.top_element = self.lst[len(self.lst)-1]
            showinfo(title="Top Candy", message=f"{self.top_element}")
            print(self.top_element)


# ___________________________________________________________________________________________________
if __name__ == "__main__":
    dispenser = Candy()
    dispenser.mainloop()
