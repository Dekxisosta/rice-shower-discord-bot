import discord
from factories.command_embed_factory import create

class PageDropdown(discord.ui.Select):
    def __init__(self, commands: dict):
        self.commands = commands
        options = [
            discord.SelectOption(
                label=cmd_name,
                description=cmd_data.get("desc", "No description provided."),
                value=cmd_name
            )
            for cmd_name, cmd_data in commands.items()
        ]
        super().__init__(placeholder="Select a command for more information", min_values=1, max_values=1, options=options)

    def set_commands(self, commands: dict):
        self.options = [
            discord.SelectOption(
                label=cmd_name,
                description=cmd_data.get("desc", "No description provided."),
                value=cmd_name
            )
            for cmd_name, cmd_data in commands.items()
        ]
        self.values.clear()

    async def callback(self, interaction: discord.Interaction):
        selected_cmd = self.values[0]
        cmd_data = self.commands[selected_cmd]

        embed = create(
            cmd_name=selected_cmd,
            desc=cmd_data["desc"],
            usage=cmd_data.get("usage", "No usage provided."),
            more_desc=cmd_data.get("more-desc"),
            more_usage=cmd_data.get("more-usage")
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )