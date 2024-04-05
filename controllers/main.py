from models.main import Model
from models.auth import Auth, User

from .dbsend import DbSend
from views.main import View

from .home import HomeController
from .signin import SignInController
from .signup import SignUpController
from .patients import PatientsController
from .doctors import DoctorsController


class Controller:
    current_user: User  # Define global variable to store current user

    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.signin_controller = SignInController(model, view)
        self.signup_controller = SignUpController(model, view)
        self.home_controller = HomeController(model, view)
        self.patients_controller = PatientsController(model, view)
        self.doctors_controller = DoctorsController(model, view)

        self.model.auth.add_event_listener("auth_changed", self.auth_state_listener)

    def auth_state_listener(self, data: Auth) -> None:
        if data.is_logged_in:
            # User is logged in, add user to session
            self.add_user_to_session(data.current_user)
            self.home_controller.update_view()
            self.view.switch("home")
        else:
            # User logged out, remove user from session
            self.remove_user_from_session()
            self.view.switch("signin")

    @classmethod
    def add_user_to_session(cls, user: User) -> None:
        # Store user in global variable
        cls.current_user = user

    @classmethod
    def remove_user_from_session(cls) -> None:
        # Clear user from global variable
        cls.current_user = None

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            # User is already logged in, add user to session
            self.add_user_to_session(self.model.auth.current_user)
            self.view.switch("home")
        else:
            self.view.switch("signin")

        self.view.start_mainloop()
