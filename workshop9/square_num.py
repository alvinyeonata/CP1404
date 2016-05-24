from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class SquareNumberApp(App):


    def build(self):
        Window.size = (400, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('square_num_txt.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = float(self.root.ids.input_number.text)
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
