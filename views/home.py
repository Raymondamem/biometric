from tkinter import Frame, Label, Button, Entry 
from tkinter import *
from PIL import Image, ImageTk

class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.signout_btn = Button(self, text="Sign Out" , fg='red', bg='yellow')
        self.signout_btn.grid(row=3, column=0, padx=10, pady=10)

        self.pat_img = ImageTk.PhotoImage(Image.open('images/patient.jpeg'))
        self.patients_btn = Button(self, text="Patients", image=self.pat_img,)
        self.patients_btn.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.doc_img = ImageTk.PhotoImage(Image.open('images/doctor.jpeg'))
        self.doctors_btn = Button(self, text="Doctors", image=self.doc_img)
        self.doctors_btn.grid(row=4, column=0, padx=10, pady=10, sticky='e')


