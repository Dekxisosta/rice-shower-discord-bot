from discord.ext import commands
from data import session_data as db
from resources.responses import RS_CALLOUT_LINES
from resources.triggers import USER_GREETINGS

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
        
        content = msg.content.lower()
        
        if "rice shower" in content and any(g in content for g in USER_GREETINGS):
            if db.callout_line_count >= len(RS_CALLOUT_LINES):
                db.callout_line_count+=1

            await msg.channel.send(RS_CALLOUT_LINES[db.callout_line_count])

            db.callout_line_count += 1

async def setup(bot):
    await bot.add_cog(OnMessage(bot))