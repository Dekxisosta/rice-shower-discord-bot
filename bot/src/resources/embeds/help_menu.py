from pathlib import Path
from resources.descriptions.general_command_desc import DESC
from config.constants.defaults import DEFAULT_PREFIX
import discord

# Path to PNG folder
PNG_DIR = Path(__file__).parent.parent / "pngs"

def get_embed():
    banner_file = discord.File(PNG_DIR / "commands_banner.png", filename="commands_banner.png")
    icon_file = discord.File(PNG_DIR / "profile.png", filename="profile.png")

    banner_embed = discord.Embed(
        color=discord.Color.dark_magenta()
    )
    banner_embed.set_image(url="attachment://commands_banner.png")
    banner_embed.set_footer(
        text="Rice Bot • v0.3 • Found a bug? Contact rroquxii@gmail.com",
        icon_url="attachment://profile.png"
    )

    embed = discord.Embed(
        title="🌾 **Rice Shower Bot Commands**",
        description="Here are all the things Rice can help you with, Trainer-san!",
        color=discord.Color.dark_magenta()
    )

    for cmd_name, cmd_desc in DESC.items():
        if cmd_name == "main":
            continue
        embed.add_field(name=f"```🥕/{cmd_name} | {DEFAULT_PREFIX}{cmd_name}```", value=cmd_desc, inline=True)

    return [banner_embed, embed], [banner_file, icon_file]  # return the embed and list of files to send
