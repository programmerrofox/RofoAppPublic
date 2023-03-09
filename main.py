
from kivymd.uix.boxlayout import MDBoxLayout


from screens.test_scr import Test_Scr
from screens.loaddata import LoadData
from screens.database.add_data import ConnectData
from screens.users.login_users import LoginScreen
from screens.createuser import CreateUser
from screens.add_item import Add_Item

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.list import IRightBodyTouch
from kivy.lang import Builder
#import arabic_reshaper
#import bidi.algorithm


class Container(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True


Window.size = (360, 600)
# def connect_to_database(self):
# def create_table(cursor):
#	cursor.execute("""
#	CREATE TABLE product(
#	ID INTEGER PRIMARY KEY AUTOINCREMENT,
#	name text not null,
#	age int not null,
#	mobile int not null
#	)
#	""")


Builder.load_file("interface.kv")


class MainWid(ScreenManager):
    def __init__(self, **kwarg):
        super(MainWid, self).__init__()

        self.LoginScreen = LoginScreen(self)
        self.CreateUser = CreateUser(self)
        self.StartWid = StartWid(self)
        self.MainWidow = MainWidow(self)
        self.LoadData = LoadData(self)
        self.Multiadd_Scr = Multiadd_Scr(self)
        self.Test_Scr = Test_Scr(self)
        self.Add_Item = Add_Item(self)

        wid = Screen(name='start')
        wid.add_widget(self.StartWid)
        self.add_widget(wid)

        wid = Screen(name='login')
        wid.add_widget(self.LoginScreen)
        self.add_widget(wid)

        wid = Screen(name='createuser')
        wid.add_widget(self.CreateUser)
        self.add_widget(wid)

        wid = Screen(name='mainwindow')
        wid.add_widget(self.MainWidow)
        self.add_widget(wid)

        wid = Screen(name='loaddata')
        wid.add_widget(self.LoadData)
        self.add_widget(wid)

        wid = Screen(name='multiaddscr')
        wid.add_widget(self.Multiadd_Scr)
        self.add_widget(wid)

        wid = Screen(name='testscr')
        wid.add_widget(self.Test_Scr)
        self.add_widget(wid)

        wid = Screen(name='additem')
        wid.add_widget(self.Add_Item)
        self.add_widget(wid)

        self.goto_screen('start')

    def goto_screen(self, name):
        self.current = name



class LoginScreen(MDBoxLayout):

    def __init__(self, mainwid, **kwargs):
        super(LoginScreen, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)

    def validate_user(self):
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
                self.mainwid.goto_screen('mainwindow')



class CreateUser(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(CreateUser, self).__init__()
        self.mainwid = mainwid


    def validate_users(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        pwd2= self.ids.txt_confirm
        info = self.ids.info

        uname = user.text
        passw = pwd.text
        passw2= pwd2.text


        if (uname == '' or passw == ''):
            info.text = 'invaled user name or password ya man]'


        elif (passw != passw2):
            info.text = 'confirm password error'

        else:
            self.insert_usersdata(uname,passw)
            info.text = 'user created successful'
            user.text =''
            pwd.text =''
            pwd2.text=''


    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)


    def insert_usersdata(self,username,password):
        inserdata = ConnectData()
        inserdata.insert_data(username,password)



class LoadData(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(LoadData, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)



class Multiadd_Scr(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Multiadd_Scr, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)


class Test_Scr(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Test_Scr, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)


class StartWid(BoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(StartWid, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)


class Add_Item(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Add_Item, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)

# ========================================================================
class MainWidow(BoxLayout, Screen):
    def __init__(self, mainwid, **kwargs):
        super(MainWidow, self).__init__()
        self.mainwid = mainwid

    def create_screen(self, sc_name):
        self.mainwid.goto_screen(sc_name)





class mainapp(MDApp):
    title = 'RofoApp'

    def build(self):
        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.colors = colors
        # self.theme_cls.primary_palette = "Green"
        # self.theme_cls.accent_palette = "Green"
        return MainWid()


if __name__ == '__main__':
    mainapp().run()
