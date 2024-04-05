from models.main import Model
from views.main import View


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
       
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signout_btn.config(command=self.logout)
        self.frame.patients_btn.config(command=self.patients)
        self.frame.doctors_btn.config(command=self.doctors)

    def logout(self) -> None:
        self.model.auth.logout()

    def patients(self) -> None:
        self.view.switch("patients")

    def doctors(self) -> None:
        self.view.switch("doctors")
     

    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            username = current_user["username"]
            self.frame.greeting.config(text=f"Welcome, {username}!")
        else:
            self.frame.greeting.config(text=f"")
