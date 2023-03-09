from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.app import App

Builder.load_file("screens/users/login_users.kv")

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_users_create(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if (uname == '' or passw == ''):
            info.text = 'from createuser.py file]'
        else:
            if (uname == 'admin' and passw == 'admin'):
                info.text = 'Logged In succesfully'


class Login_Users(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    sa = Login_Users()
    sa.run()
