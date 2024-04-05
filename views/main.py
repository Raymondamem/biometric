from typing import TypedDict
from tkinter import messagebox  # Import messagebox for error messages

from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView
from .patients import PatientsView
from .doctors import DoctorsView
from .success_popup import SuccessPopup

class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView
    patients: PatientsView
    doctors: DoctorsView

class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignUpView, "signup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(PatientsView, "patients")
        self._add_frame(DoctorsView, "doctors")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()

    def show_error_message(self, message: str) -> None:
        messagebox.showerror("Error", message)

    def show_success_popup(self, message: str) -> None:
        popup = SuccessPopup(message)
        popup.grab_set()  # Make the popup modal
        self.root.wait_window(popup)  # Wait for the popup to close
