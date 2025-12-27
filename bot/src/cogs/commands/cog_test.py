import discord
from discord.ext import commands

class PageView(discord.ui.View):
    def __init__(self, pages):
        super().__init__(timeout=None)
        self.pages = pages
        self.current = 0

    @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current = (self.current - 1) % len(self.pages)
        await interaction.response.edit_message(content=self.pages[self.current], view=self)

    @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current = (self.current + 1) % len(self.pages)
        await interaction.response.edit_message(content=self.pages[self.current], view=self)

class NavigationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="pages",
        description="Show a message with previous/next buttons"
    )
    async def pages(self, ctx: commands.Context):
        pages = ["Page 1: Hello!", "Page 2: How are you?", "Page 3: Goodbye!"]
        view = PageView(pages)
        await ctx.send(pages[0], view=view)


async def setup(bot):
    await bot.add_cog(NavigationCog(bot))