from .command import Command


def noop():
    pass


def get_builtin_commands():

    return [
        Command(
            name="help",
            description="Mostrar comandos disponíveis",
            handler=noop,
        ),
        Command(
            name="open",
            description="Abrir arquivo",
            handler=noop,
        ),
        Command(
            name="terminal",
            description="Abrir terminal",
            handler=noop,
        ),
        Command(
            name="settings",
            description="Abrir configurações",
            handler=noop,
        ),
    ]