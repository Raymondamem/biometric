from tkinter import Frame, Label, Button, ttk
from tkinter import *
from controllers.dbsend import DbSend

class PatientsView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Home")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.greeting = Label(self, text="")
        self.greeting.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

       

        top_frame = Frame(self, bg='blue', width=800, height=50, pady=3)
        top_frame.grid(row=0, sticky="ew")

        center_right = Frame(self, bg='grey', width=100, height=100, padx=3, pady=3)
        center_right.grid(row=2, column=1)

        center_left = Frame(self, bg='grey', width=100, height=100, padx=3, pady=3)
        center_left.grid(row=1, column=0)

        imp = Button(top_frame, text='Add Patient', command  = lambda: popwin(self))
        imp.grid(column=0, row=0, padx=5, pady=0)

        self.signout_btn = Button(top_frame, text="Sign Out")
        self.signout_btn.grid(row=0, column=1, padx=10, pady=10)

       


        patient_list = LabelFrame(center_left, text="Patient List")
        patient_list.pack(fill="both", expand="yes", padx="20",pady="10")

        trv = ttk.Treeview(patient_list, columns=(1,2,3), show="headings", height="8")
        trv.pack()
        
        trv.heading(1, text="Name")
        trv.heading(2, text="Hospital Number")
        trv.heading(3, text="Phone Number")


def popwin(self):
    top = Toplevel(self)
    top.geometry("400x500")
    top.title("Add New Patient")


    global fname 
    global lname 
    global hnum
    global phone
    
    fname = StringVar()
    lname = StringVar()
    hnum = StringVar()
    phone = StringVar()

    wrapper2 = LabelFrame(top, text="Data parameters")
    wrapper3 = LabelFrame(top, text="Well Perimeter")

    wrapper2.pack(fill="both", expand="yes", padx="20",pady="10")

    
    imp = ttk.Button(wrapper2, text='ADD', command = DbSend.send_patients(fname.get(), lname.get()))
    #new_button.pack()
    imp.grid(column=0, row=8, padx=5, pady=0)
    
    imp = ttk.Button(wrapper2, text='Cancel', command  = lambda: addtab("buildup"))
    #new_button.pack()
    imp.grid(column=1, row=8, padx=5, pady=0)
    
    
    first_name = Label(wrapper2, text = 'First Name', font=('calibre',10, 'bold'))
    U_ = Entry(wrapper2,textvariable = fname, font=('calibre',10,'normal'))
    first_name.grid(row=0,column=0)
    U_.grid(row=1,column=0)
    

    last_name = Label(wrapper2, text = 'Last Name', font=('calibre',10, 'bold'))
    Bo_ = Entry(wrapper2,textvariable = lname, font=('calibre',10,'normal'))
    last_name.grid(row=0,column=1)
    Bo_.grid(row=1,column=1)
    
   
    hospital_number = Label(wrapper2, text = 'Hospital Number', font=('calibre',10, 'bold'))
    ct_ = Entry(wrapper2,textvariable = hnum, font=('calibre',10,'normal'))
    hospital_number.grid(row=0,column=2)
    ct_.grid(row=1,column=2)
    

    phone_number = Label(wrapper2, text = 'Phone Number', font=('calibre',10, 'bold'))
    Qo_ = Entry(wrapper2,textvariable = phone, font=('calibre',10,'normal'))
    phone_number.grid(row=2,column=0)
    Qo_.grid(row=3,column=0)
    

    pass



      