from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TicTacToeApp(App):
    def build(self):
        self.title = "لعبة إكس أو"
        self.turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        layout = GridLayout(cols=3)
        self.btns = []
        for i in range(9):
            btn = Button(text='', font_size=50)
            btn.bind(on_release=self.on_click)
            layout.add_widget(btn)
            self.btns.append(btn)
        return layout

    def on_click(self, btn):
        if btn.text == '':
            btn.text = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'

if __name__ == '__main__':
    TicTacToeApp().run()
