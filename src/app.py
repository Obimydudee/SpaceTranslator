import discord
from discord.ext import commands
import os

TOKEN = os.getenv("Space")

_version = "1.0"
_developer = "obi1, .weevef"
_botname = "SpaceTranslator"

class MyClient(commands.Bot):
    def __init__(self):
        intent=discord.Intents.default()
        super().__init__(intents=intent, command_prefix="!")

    async def setup_hook(self):
        cogs = os.path.join(os.path.dirname(os.path.realpath(__file__)), "cogs")
        for filename in os.listdir(cogs):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                try:
                   await self.load_extension(f"cogs.{module_name}")
                except Exception as e:
                    print(f"Failed to load extension {module_name}: {e}")


    async def on_ready(self):
        await self.tree.sync()
        await self.change_presence(activity=discord.CustomActivity(name="Space awaits you!"))


client = MyClient()
client.run(TOKEN)