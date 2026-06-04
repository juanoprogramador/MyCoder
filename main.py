from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TextArea

class MyCoder(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield TextArea()
        yield Footer()

if __name__ == "__main__":
    MyCoder().run()