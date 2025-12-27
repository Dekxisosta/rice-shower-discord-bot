from pathlib import Path
import discord

# Path to PNG folder
PNG_DIR = Path(__file__).parent.parent.parent / "images"

def create(
        bot_prefix:str, 
        desc: str, 
        commands: dict,
        group_prefix: str | None = None, 
        ):
    embed = discord.Embed(
        title="🪻 **Rice Shower Bot Commands**",
        description="Here are all the things Rice can help you with, Trainer-san!",
        color=discord.Color.dark_magenta()
    )
    if group_prefix is not None:
        embed.add_field(
            name=f"🪻Prefix Command Group: {group_prefix}",
            value=f"\"{desc}\"",
            inline=False
        )
    else:
        embed.add_field(
            name=f"🪻Set of Available Commands",
            value=f"\"{desc}\"",
            inline=False
        )

    for cmd_name, _ in commands.items():
        if cmd_name == "main":
            continue
        if group_prefix is None:
            embed.add_field(
                name=f"```🥕/{cmd_name} | {bot_prefix}{cmd_name}```", 
                value=commands[cmd_name]["desc"], 
                inline=True)
        else:
            embed.add_field(
                name=f"```🥕/{group_prefix} {cmd_name} | {bot_prefix}{group_prefix} {cmd_name}```", 
                value=commands[cmd_name]["desc"], 
                inline=True)

    return embed