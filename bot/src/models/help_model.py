from discord import Embed

class HelpGroup():
    def __init__(self, embed: Embed, commands: dict):
        self.embed = embed
        self.commands = commands