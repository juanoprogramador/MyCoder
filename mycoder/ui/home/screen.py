from pathlib import Path

from textual.screen import Screen
from textual.widgets import Static

from mycoder.ui.home.command_palette import CommandPalette

from mycoder.core.commands.registry import CommandRegistry
from mycoder.core.commands.builtin import get_builtin_commands

BANNER = r"""
███╗   ███╗██╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗
████╗ ████║╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║ ╚████╔╝ ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║╚██╔╝██║  ╚██╔╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║   ██║   ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚═╝     ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

class HomeScreen(Screen):

    def compose(self):

        registry = CommandRegistry()

        for command in get_builtin_commands():
            registry.register(command)

        yield Static(BANNER)

        yield Static(
            f"Workspace: {Path.cwd()}"
        )

        yield CommandPalette(registry)