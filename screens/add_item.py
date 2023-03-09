#from kivymd.uix.boxlayout import MDBoxLayout
#from kivy.lang import Builder

#class Add_Item(MDBoxLayout):
    #Builder.load_file("screens/add_item.kv")
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file("screens/add_item.kv")



class Add_Item(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == '__main__':
    sa = Default()
    sa.run()

