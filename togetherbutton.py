from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MinhaApp(App):
    def build(self):
        return ToggleButton(text='ligado', state='normal')
    
if __name__ == "__main__":
    MinhaApp().run()