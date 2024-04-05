from models.main import Model
from models.auth import User
from views.main import View
from .dbsend import DbSend


class SignUpController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self.db_sender = DbSend()
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signup_btn.config(command=self.signup)
        self.frame.signin_btn.config(command=self.signin)

    def signin(self) -> None:
        self.view.switch("signin")

    def signup(self) -> None:
        fullName = self.frame.fullname_input.get()
        userName = self.frame.username_input.get()
        passWord = self.frame.password_input.get()
        hasAgreed = self.frame.has_agreed.get()

        if not fullName or not userName or not passWord or not hasAgreed:
            self.view.show_error_message(f"Invalid entry, Empty Credentials!")
            return
        elif len(passWord) < 5:
            self.view.show_error_message(
                f"Invalid entry, Password must be greater than 6 char!"
            )
            return
        elif len(fullName) <= 3 or len(userName) <= 3:
            self.view.show_error_message(f"Invalid entry, No Achronym allowed!")
            return

        elif self.db_sender.check_username_exist(userName) == -2:
            self.view.show_error_message("No database connection!!!")
            return
        elif self.db_sender.check_username_exist(userName):
            self.view.show_error_message(
                "Username already exists. Please choose another."
            )
            return

        self.db_sender.insert_user(userName, passWord, fullName)
        self.view.show_success_popup("Signup successful! You can now sign in.")
        self.clear_form()
        data = {
            "fullname": fullName,
            "username": userName,
            "password": passWord,
            "has_agreed": hasAgreed,
        }
        print(data)
        user: User = {"username": data["username"]}
        self.model.auth.login(user)

    def clear_form(self) -> None:
        fullname = self.frame.fullname_input.get()
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()
        self.frame.fullname_input.delete(0, last=len(fullname))
        self.frame.fullname_input.focus()
        self.frame.username_input.delete(0, last=len(username))
        self.frame.password_input.delete(0, last=len(password))

        self.frame.has_agreed.set(False)
