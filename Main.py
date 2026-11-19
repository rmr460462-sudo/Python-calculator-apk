from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.display = TextInput(
            text="",
            multiline=False,
            readonly=True,
            halign="right",
            font_size=42,
            size_hint=(1, 0.25),
        )
        self.add_widget(self.display)

        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        grid = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))

        for row in buttons:
            for label in row:
                btn = Button(
                    text=label,
                    font_size=28,
                    on_press=self.on_button_press,
                )
                grid.add_widget(btn)

        self.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""
        elif text == "⌫":
            self.display.text = self.display.text[:-1]
        elif text == "=":
            try:
                allowed = set("0123456789+-*/(). ")
                if not self.display.text or not set(self.display.text).issubset(allowed):
                    self.display.text = "Error"
                    return
                result = str(eval(self.display.text))
                self.display.text = result
            except ZeroDivisionError:
                self.display.text = "০ দিয়ে ভাগ হয় না"
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += text


class CalculatorApp(App):
    def build(self):
        self.title = "ক্যালকুলেটর"
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
