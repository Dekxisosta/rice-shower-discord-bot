from discord.ext import commands
from ui.page_view import PageView

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