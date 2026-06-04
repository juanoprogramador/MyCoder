from textual.containers import Vertical
from textual.widgets import Input, ListView, ListItem, Label

from mycoder.core.commands.registry import CommandRegistry


class CommandPalette(Vertical):

    def __init__(self, registry: CommandRegistry):
        super().__init__()
        self.registry = registry

    def compose(self):

        yield Input(
            placeholder="Digite um comando..."
        )

        items = []

        for command in self.registry.all():
            items.append(
                ListItem(
                    Label(
                        f"{command.name} - {command.description}"
                    )
                )
            )

        yield ListView(*items)