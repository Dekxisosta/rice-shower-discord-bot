from discord.ext import commands
from resources import responses
from utils.console_logger import log
class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        log(f"Successfully deployed Rice Shower bot online in Discord", module_name="ON_READY", success = True)
        print(f"🥕 [{self.bot.user}] : Gotta give it my all today, Trainer-san!")

async def setup(bot):
    await bot.add_cog(OnReady(bot))