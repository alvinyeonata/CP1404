from kivy.app import App
from kivy.lang import Builder
MILES_TO_KM = 1.60934

class ConvertMilesToKilometre(App):
    def build(self):
        self.title = "Miles to Km converter"
        self.root = Builder.load_file("km_m_converter.kv")
        return self.root

    def add_or_min(self,change):
        value = self.change_to_float() + change
        self.root.ids.input_num.text = str(value)
        self.calculate()

    def calculate(self):
        value = self.change_to_float()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def change_to_float(self):
        try:
            value = float(self.root.ids.input_num.text)
            return value
        except ValueError:
            return 0

ConvertMilesToKilometre().run()