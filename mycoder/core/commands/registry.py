from .command import Command

class CommandRegistry:

    def __init__(self):
        self.__commands = {}

    def register(self, command: Command):
        self.__commands[command.name] = command

    def get(self, name: str):
        return self.__commands.get(name)
    
    def all(self):
        return list(self.__commands.values())
    
    