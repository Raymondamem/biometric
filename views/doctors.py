from tkinter import messagebox, Frame, Label, Button, ttk, Toplevel, Entry, LabelFrame
from .success_popup import SuccessPopup
from controllers.dbsend import DbSend


class DoctorsView(Frame):
    def __init__(self, root, *args, **kwargs):
        self.root = root  # Store the root Tkinter window
        self.db_sender = DbSend()
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.header = Label(self, text="Home")
        self.header.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        top_frame = Frame(self, bg="blue", width=800, height=50, pady=3)
        top_frame.grid(row=0, sticky="ew")

        center_right = Frame(self, bg="grey", width=100, height=100, padx=3, pady=3)
        center_right.grid(row=2, column=1)

        center_left = Frame(self, bg="grey", width=100, height=100, padx=3, pady=3)
        center_left.grid(row=1, column=0)

        self.imp = Button(top_frame, text="Add Patient")  # Button for adding patient
        self.imp.grid(column=0, row=0, padx=5, pady=0)
        self.imp.config(command=self.open_add_patient_popup)

        self.signout_btn = Button(top_frame, text="Sign Out")
        self.signout_btn.grid(row=0, column=1, padx=10, pady=10)

        self.patient_list = LabelFrame(center_left, text="Patient List")
        self.patient_list.pack(fill="both", expand="yes", padx="20", pady="10")

        self.trv = ttk.Treeview(
            self.patient_list, columns=(1, 2, 3), show="headings", height="8"
        )
        self.trv.pack()

        self.trv.heading(1, text="Name")
        self.trv.heading(2, text="Hospital Number")
        self.trv.heading(3, text="Phone Number")

        self.update_patient_list()  # Call the method to update the patient list initially

    def update_patient_list(self):
        # Clear existing entries in the treeview
        for i in self.trv.get_children():
            self.trv.delete(i)

        try:
            # Fetch patient list from the database using DbSend
            patient_data = self.db_sender.fetch_patient_list()

            # Populate the treeview with the fetched data
            for patient in patient_data:
                formatted_patient = " ".join(patient[1:3])  # Join first and last names
                self.trv.insert(
                    "", "end", values=(formatted_patient, patient[3], patient[4])
                )
        except Exception as e:
            print("Error fetching patient list:", e)

    def show_error_message(self, message: str) -> None:
        messagebox.showerror("Error", message)

    def show_success_popup(self, message: str) -> None:
        popup = SuccessPopup(message)
        popup.grab_set()  # Make the popup modal
        self.root.wait_window(popup)  # Wait for the popup to close

    def open_add_patient_popup(self):
        top = Toplevel(self)
        top.geometry("400x200")
        top.title("Add New Patient")

        first_name_label = Label(top, text="First Name:")
        first_name_label.grid(row=0, column=0, padx=10, pady=10)
        first_name_entry = Entry(top)
        first_name_entry.grid(row=0, column=1, padx=10, pady=10)

        last_name_label = Label(top, text="Last Name:")
        last_name_label.grid(row=1, column=0, padx=10, pady=10)
        last_name_entry = Entry(top)
        last_name_entry.grid(row=1, column=1, padx=10, pady=10)

        hospital_number_label = Label(top, text="Hospital Number:")
        hospital_number_label.grid(row=2, column=0, padx=10, pady=10)
        hospital_number_entry = Entry(top)
        hospital_number_entry.grid(row=2, column=1, padx=10, pady=10)

        phone_number_label = Label(top, text="Phone Number:")
        phone_number_label.grid(row=3, column=0, padx=10, pady=10)
        phone_number_entry = Entry(top)
        phone_number_entry.grid(row=3, column=1, padx=10, pady=10)

        add_button = Button(
            top,
            text="Add Patient",
            command=lambda: self.add_patient(
                first_name_entry.get(),
                last_name_entry.get(),
                hospital_number_entry.get(),
                phone_number_entry.get(),
            ),
        )
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_patient(self, first_name, last_name, hospital_number, phone_number):
        # handle errors
        if not first_name or not last_name or not hospital_number or not phone_number:
            self.show_error_message(f"Invalid entry, Empty Credentials!")
            return
        elif len(first_name) <= 3 or len(last_name) <= 3 or len(hospital_number) <= 3:
            self.show_error_message(f"Invalid entry, No Achronym allowed!")
            return
        elif len(phone_number) != 11:
            self.show_error_message(f"Invalid entry, Enter valid Number!")
            return
        elif self.db_sender.check_patients_exist(int(phone_number)) == -2:
            self.show_error_message(f"No database connection!!!")
            return
        elif self.db_sender.check_patients_exist(int(phone_number)):  # not working yet
            self.show_error_message(
                "Patient already exists. Please enter another patient."
            )
            return
        # no errors so add
        self.db_sender.insert_patient(
            first_name, last_name, hospital_number, phone_number
        )
        # After adding patient, update the patient list in the treeview
        self.update_patient_list()
        self.show_success_popup("Patient successful added!")
