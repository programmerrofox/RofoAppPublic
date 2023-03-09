from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file("screens/createuser.kv")



class CreateUser(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def validate_users_create(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if (uname == '' or passw == ''):
            info.text = 'invaled user name or password]'
        else:
            if (uname == 'admin' and passw == 'admin'):
                info.text = 'Logged In succesfully'

class ConnectData():
    def add_data(self, name):
        print(name)

class Default(App):
    def build(self):
        return CreateUser()


if __name__ == '__main__':
    sa = Default()
    sa.run()

