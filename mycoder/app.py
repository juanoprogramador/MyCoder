from textual.app import App

from mycoder.ui.home.screen import HomeScreen

class MyCoder(App):

    def on_mount(self):
        self.push_screen(HomeScreen())


def main():
    MyCoder().run()