import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class grid(GridLayout):
    def __init__(self,**kwargs):
        super(grid,self).__init__(**kwargs)
        self.cols=1
        self.sec_grid=GridLayout()
        self.sec_grid.cols=2
        self.sec_grid.add_widget(Label(text="Name :"))
        self.name=TextInput(multiline=False)
        self.sec_grid.add_widget(self.name)
        self.sec_grid.add_widget(Label(text="Roll No :-"))
        self.roll=TextInput(multiline=False)
        self.sec_grid.add_widget(self.roll)
        self.add_widget(self.sec_grid)
        self.submit=Button(text="Submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        name=self.name.text
        roll=self.roll.text
        self.add_widget(Label(text=name))
        self.name.text=""
        self.roll.text=""

class myApp(App):
    def build(self):
        return grid()
    



if __name__=="__main__":
    myApp().run()
















