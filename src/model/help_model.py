from discord import Embed

class CommandHelpGroup():
    def __init__(self, embed: Embed, commands: dict):
        self.embed = embed
        self.commands = commands