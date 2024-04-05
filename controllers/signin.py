from models.main import Model
from models.auth import User
from views.main import View
from .dbsend import DbSend


class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self.db_sender = DbSend()
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signin_btn.config(command=self.signin)
        self.frame.signup_btn.config(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_input.get()
        password = self.frame.password_input.get()

        if not username or not password:
            self.view.show_error_message("Invalid, Empty credentials!")
            return
        elif self.db_sender.check_user_credentials(username, password) == -2:
            self.view.show_error_message("No database connection!!!")
            return
        elif self.db_sender.check_user_credentials(username, password):
            self.view.show_success_popup("Signin successful!...")
            data = {"username": username, "password": password}
            print(f"{data}  {len(username)}")
            self.frame.password_input.delete(0, last=len(password))
            user: User = {"username": data["username"]}
            self.model.auth.login(user)
        else:
            self.view.show_error_message("Invalid entry, No Such User, SignUp!")
