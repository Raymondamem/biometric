import tkinter as tk


class SuccessPopup(tk.Toplevel):
    def __init__(self, message):
        super().__init__()
        self.title("Success")
        self.geometry("300x100")

        label = tk.Label(self, text=message, padx=20, pady=20)
        label.pack()

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)
