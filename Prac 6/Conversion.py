from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class Conversion(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Square Number"
        self.root = Builder.load_file('Conversion.kv')
        return self.root

    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        new_increment = value + 1
        self.root.ids.output_label.text =str(new_increment)



Conversion().run()