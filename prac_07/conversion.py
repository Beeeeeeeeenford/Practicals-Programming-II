

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConversionApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('conversion.kv')
        return self.root

    def handle_convert(self, value):
        result = value * 1.609
        self.root.ids.output_label.text = str(result)

    def handle_up(self, value):
        new_value = value + 1
        self.root.ids.input_number.text = new_value

    def handle_down(self, value):
        new_value = value - 1
        self.root.ids.input_number.text = new_value


ConversionApp().run()
