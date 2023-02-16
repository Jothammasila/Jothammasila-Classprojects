import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import simpledialog

class Dice(tk.Tk):

    def __init__(self):
        super().__init__()

        global die_dict
        self.die_dict = {}
        
        #---------counters---------------------------------------
        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0
        self.counter4 = 0
        self.counter5 = 0
        self.counter6 = 0

        self.counter =0
        
            # configure the root window
        self.title("Dice Roller")
        self.geometry('480x640')
        self.configure(background="Grey")

        self.canvas = tk.Canvas(
            self, width=1500, height=300, background="grey13", state="normal")
        self.canvas.pack()
        
# ------------------BUTTONS--------------------------------------------------------
        ttk.Button(self, text="Rolls",
                   command=self.roll).place(relx=.05, rely=.6)
                   
# ----------------------------ENTER THE NUMBER OF DICE / ROLLS-----------------------

    def roll(self):
        global random_outcome
        if True:
            self.rollNumber = simpledialog.askinteger(
                title="Rolling", prompt="Dice")

            self.random_outcome = [random.random()
                                   for x in range(self.rollNumber)]
# ----------------------RESULTS TABULATION--------------------------------------------

            del self.canvas

            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="grey13", state="normal")
            self.canvas.pack()
            self.canvas.place(x=200, y=15)

            self.table = ttk.Treeview(self.canvas, columns=('face', 'frequency', 'percentage'),
                                      show='headings')

            self.table.heading('face', text='Faces')
            self.table.heading('frequency', text='Frequency')
            self.table.heading('percentage', text='Percentage')
            self.table.pack()
            
            self.face_range = 1/6
            self.face_range = round(self.face_range,2)
            for i in self.random_outcome:

                if i > 0.0 and i < self.face_range:
                    self.counter1 +=1

                elif i > self.face_range and i < self.face_range *2:
                    self.counter2 +=1

                elif i > self.face_range *2 and i < self.face_range *3:
                    self.counter3 +=1

                elif i > self.face_range *3 and i < self.face_range*4:
                    self.counter4 +=1

                elif i > self.face_range *4 and i < self.face_range *5:
                    self.counter5 +=1

                elif i > self.face_range *5:
                    self.counter6 +=1



                self.die_dict[1] = self.counter1 
                self.die_dict[2] = self.counter2 
                self.die_dict[3] = self.counter3 
                self.die_dict[4] = self.counter4 
                self.die_dict[5] = self.counter5 
                self.die_dict[6] = self.counter6

            self.percentage_list = list()
            self.frequency_list = list()

            for key in self.die_dict.keys():
                print(f"{key} | {self.die_dict[key]}")
                self.percentage = self.die_dict[key] / \
                    len(self.random_outcome)*100
                self.frequency_list.append(self.die_dict[key])
                self.percentage_list.append(self.percentage)

                self.data = (
                    key, self.die_dict[key], f"{self.percentage:0.2f}")

                self.table.insert(parent="", index="end", values=self.data)
            self.table.insert(parent="", index="end", values=("", f"Σ ={sum(self.frequency_list)}", f"Σ ={sum(self.percentage_list):0.2f}"))

if __name__ == "__main__":
    dice = Dice()
    dice.mainloop()
