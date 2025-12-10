import discord
def rice_menu_embed():
    embed = discord.Embed(
        title="🐴 Rice Shower Command List",
        description="Here are all the things Rice can help you with, Trainer-san!",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="💠 Greeting",
        value="`!rice greet` — Rice shyly responds to your call.",
        inline=False
    )

    embed.add_field(
        name="⏳ Timer",
        value="`!rice timer <seconds>` — Starts a countdown timer.",
        inline=False
    )

    embed.add_field(
        name="🎭 Mood",
        value="`!rice mood` — Shows Rice’s current emotional state… nervously.",
        inline=False
    )

    embed.add_field(
        name="🎐 Joke",
        value="`!rice joke` — Rice attempts to… humor you?",
        inline=False
    )

    embed.add_field(
        name="🏇 Training",
        value="`!rice train` — Train Rice to improve her stats!",
        inline=False
    )

    embed.add_field(
        name="📘 Help",
        value="`!rice help` — Shows this help menu.",
        inline=False
    )

    embed.set_footer(text="Have fun with Rice Shower! 💙")
    embed.set_thumbnail(url="https://i.imgur.com/2RZ9oAv.png") 

    return embed


RICE_MENU_EMBED = rice_menu_embed()