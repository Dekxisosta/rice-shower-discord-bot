import discord
from discord.ui import View
from ui.page_dropdown import PageDropdown

class PageView(View):
    def __init__(self, pages: list[discord.Embed]):
        super().__init__(timeout=None)
        self.pages = pages
        self.current = 0
        self.update_pagination()
        self.add_item(PageDropdown(self))

    def update_pagination(self):
        self.pagination.label = f"{self.current + 1} / {len(self.pages)}"
        self.pagination.disabled = True
        
    @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current = (self.current - 1) % len(self.pages)
        self.update_pagination()
        await interaction.response.edit_message(embed=self.pages[self.current], view=self)

    @discord.ui.button(label=f"1 / 1", style=discord.ButtonStyle.grey)
    async def pagination(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

    @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current = (self.current + 1) % len(self.pages)
        self.update_pagination()
        await interaction.response.edit_message(embed=self.pages[self.current], view=self)

    @discord.ui.button(label="close", style=discord.ButtonStyle.danger)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()

    
