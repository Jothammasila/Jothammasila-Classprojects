import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
from tkinter import simpledialog


class Triage(tk.Tk):
    patients = {}

    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("Triage Hospital")
        self.geometry('480x640')
        self.configure(background="seagreen1")

        self.canvas = tk.Canvas(
            self, width=1500, height=300, background="lightcyan1", state="normal")
        self.canvas.pack()  # expand="YES",fill="both"
        #self.canvas.place(x=20, y=200)

        self.image = Image.open("./Images/Hospital.jpg")
        self.resize_hospital_image = self.image.resize(
            (180, 180), Image.ANTIALIAS)
        self.hospital = ImageTk.PhotoImage(self.resize_hospital_image)
        self.hospital_label = tk.Label(self, image=self.hospital)
        self.canvas.create_image(1250, 150, image=self.hospital)
        # self.hospital_label.pack()

        self.raw_image = Image.open("./Images/patient.png")
        self.resize_patient_image = self.raw_image.resize(
            (100, 100), Image.ANTIALIAS)
        self.patient_image = ImageTk.PhotoImage(self.resize_patient_image)
        #self.patient_label = tk.Label(self, image=self.patient_image)


# ======================== BUTTONS =============================================================
        ttk.Button(self, text="Admit",
                   command=self.Admit).place(relx=.05, rely=.6)
        ttk.Button(self, text="Patients", command=self.display_patients).place(
            relx=.12, rely=.6)
        ttk.Button(self, text="isEmpty", command=self.isEmpty).place(
            relx=.19, rely=.6)
        ttk.Button(self, text="Priority", command=self.highestPriority).place(
            relx=.26, rely=.6)
        ttk.Button(self, text="Treated", command=self.treat).place(
            relx=.33, rely=.6)
        ttk.Button(self, text="Size", command=self.sizeOfQueue).place(
            relx=.4, rely=.6)
        ttk.Button(self, text="Repace Key", command=self.replaceKey).place(
            relx=.47, rely=.6)  # removing a key associated with a patient
        ttk.Button(self, text="Rep Patient", command=self.Replace_value).place(
            relx=.54, rely=.6)
        ttk.Button(self, text="Exit", command=self.quit).place(
            relx=.61, rely=.6)


# ========================== ADMIT/POLL===================================================


    def Admit(self):

        self.admission = True
        self.constant = 1050
        self.x_pixel = 150
        #self.raw_image = Image.open("./Images/patient.png")
        # self.resize_patient_image = self.raw_image.resize(
        # (100, 100), Image.ANTIALIAS)
        #self.patient_image = ImageTk.PhotoImage(self.resize_patient_image)
        #self.patient_label = tk.Label(self, image=self.patient_image)

        while self.admission and self.constant > self.x_pixel:
            if len(list(self.patients)) == 0:
                self.severety = simpledialog.askinteger(
                    title="Patient", prompt="Age")
                self.name = simpledialog.askstring(
                    title="Patient", prompt="Name")
                self.patients[self.severety] = self.name
# -------------------------------------------------------------------------------------
                self.canvas.create_image(
                    self.constant, self.x_pixel, image=self.patient_image)
            else:
                self.severety = simpledialog.askinteger(
                    title="Patient", prompt="Age")
                self.name = simpledialog.askstring(
                    title="Patient", prompt="Name")
                self.patients[self.severety] = self.name

                self.canvas.create_image(
                    self.constant-(len(list(self.patients))*50), self.x_pixel, image=self.patient_image)

            self.constant -= self.x_pixel


# --------------------------------------------------------------------------------------

            self.another_patient = self.name = simpledialog.askstring(
                title="Patient", prompt="Admit another")

            if self.another_patient == "No".lower():
                self.admission = False


# ==================== TREAT/REMOVE MIN =========================================

    def treat(self):
        if len(self.patients) == 0:
            showinfo(title="Patients", message="None")

        elif len(self.patients) == 1:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            showinfo(title="Patients", message="Finshed!")

        elif len(self.patients) == 2:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)

        elif len(self.patients) == 3:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)
            self.canvas.create_image(900, 150, image=self.patient_image)

        elif len(self.patients) == 4:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)
            self.canvas.create_image(900, 150, image=self.patient_image)
            self.canvas.create_image(750, 150, image=self.patient_image)

        elif len(self.patients) == 5:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)
            self.canvas.create_image(900, 150, image=self.patient_image)
            self.canvas.create_image(750, 150, image=self.patient_image)
            self.canvas.create_image(600, 150, image=self.patient_image)

        elif len(self.patients) == 6:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)
            self.canvas.create_image(900, 150, image=self.patient_image)
            self.canvas.create_image(750, 150, image=self.patient_image)
            self.canvas.create_image(600, 150, image=self.patient_image)
            self.canvas.create_image(450, 150, image=self.patient_image)

        elif len(self.patients) == 7:
            del self.canvas
            del self.patients[min(list(self.patients))]
            self.canvas = tk.Canvas(
                self, width=1500, height=300, background="lightcyan1", state="normal")
            self.canvas.pack()
            self.canvas.place(x=0, y=0)
            self.canvas.create_image(1250, 150, image=self.hospital)
            self.canvas.create_image(1050, 150, image=self.patient_image)
            self.canvas.create_image(900, 150, image=self.patient_image)
            self.canvas.create_image(750, 150, image=self.patient_image)
            self.canvas.create_image(600, 150, image=self.patient_image)
            self.canvas.create_image(450, 150, image=self.patient_image)
            self.canvas.create_image(300, 150, image=self.patient_image)

        else:
            showinfo(title="Patients", message="Can't Treat")


# =================ALL PATIENTS ADMITTED====================================================


    def display_patients(self):
        self.listbox = tk.Listbox(self)
        for severity, name in self.patients.items():
           #self.listbox.insert(0, name + " :"+str(severity))
            if len(self.patients) == 0:
                showinfo(title="", message="No patient")
            else:
                showinfo(title="Patients", message=f"{name}: {severity}")


# ================ IS EMPTY==============================================================


    def isEmpty(self):
        if len(self.patients) == 0:
            showinfo(title="isEmpty?", message="True")
            return True
        else:
            showinfo(title="Is Empty", message="False")
# ============== HIGHEST PRIORITY =========================================================

    def highestPriority(self):
        if len(self.patients) == 0:
            showinfo(title="Priority", message="None")
        else:
            self.patients_list = list(self.patients.keys())
            self.min = min(self.patients_list)
            showinfo(title="Priority",
                     message=f"{self.min} : {self.patients[self.min]}")
            return

# ==================== SIZE OF THE QUEUE======================================================
    def sizeOfQueue(self):
        if len(self.patients) == 0:
            showinfo(title="Size", message=f"No Patients")
        elif len(self.patients) > 0 and len(self.patients) < 7:
            self.o_size = len(list(self.patients))
            showinfo(title="Size", message=f"{self.o_size}")
# ========================= REPLACING A KEY==================================================
    def replaceKey(self):
        self.key_to_change = simpledialog.askinteger(title="Patient", prompt="Age")
        for key in self.patients.keys():
            if key==self.key_to_change:
                self.new_key = simpledialog.askinteger(title="Patient", prompt="Age")
                self.patients[self.new_key]=self.patients.pop(key)
                showinfo(title="Key Change",message=f"{self.patients[self.new_key]}: {self.new_key}")

# ============================= REPLACING A VALUE =========================================

    def Replace_value(self):
        self.value_to_change = simpledialog.askstring(title="Patient", prompt="Name")
        for i in self.patients.keys():
            if self.patients[i]==self.value_to_change:
                self.new_value = simpledialog.askstring(title="Patient", prompt="Name")
                self.patients[i]=self.new_value
                showinfo(title="Replace",message=f"{self.value_to_change}-->{self.new_value} replaced")
                
#=============================================================================================

if __name__ == "__main__":
    hospital = Triage()
    hospital.mainloop()
