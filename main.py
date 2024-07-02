from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDTimePicker


class TimePickerApp(MDApp):
    def build(self):
        return TimePickerLayout()


class TimePickerLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.time_label = MDLabel(text="Выберите время")
        self.add_widget(self.time_label)

        self.time_button = MDFlatButton(text="Открыть TimePicker", on_release=self.show_time_picker)
        self.add_widget(self.time_button)

    def show_time_picker(self, *args):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_time(self, instance, time):
        self.time_label.text = f"Выбранное время: {time.strftime('%H:%M')}"


if __name__ == '__main__':
    TimePickerApp().run()
