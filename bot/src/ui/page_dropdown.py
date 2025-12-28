import discord

class PageDropdown(discord.ui.Select):
    def __init__(self, parent_view):
        self.parent_view = parent_view
        options = [
            discord.SelectOption(
                label=f"Page {i+1}",
                description=f"Go to page {i+1}",
                value=str(i)
            ) for i in range(len(parent_view.pages))
        ]
        super().__init__(placeholder="Select a page...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_index = int(self.values[0])
        self.parent_view.current = selected_index
        self.parent_view.update_pagination()
        await interaction.response.edit_message(
            embed=self.parent_view.pages[self.parent_view.current],
            view=self.parent_view
        )