from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

kv_string = '''
BoxLayout:
    orientation: 'vertical'

    MDRaisedButton:
        text: "Open Dialog"
        on_release: app.open_dialog()

'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(kv_string)

    def open_dialog(self):
        dialog = MDDialog(
            title="Dialog Example",
            text="Initial Text",
            buttons=[
                MDRaisedButton(
                    text="Change Text",
                    on_release=self.change_dialog_text
                ),
                MDRaisedButton(
                    text="Close Dialog",
                    on_release=self.close_dialog
                )
            ]
        )
        self.dialog = dialog  # Store the dialog as an instance variable
        dialog.open()

    def change_dialog_text(self, instance):
        new_text = "New Text"
        self.dialog.text = new_text  # Update the dialog text

    def close_dialog(self, instance):
        self.dialog.dismiss()


if __name__ == '__main__':
    DemoApp().run()
