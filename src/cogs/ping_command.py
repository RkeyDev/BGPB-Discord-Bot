import nextcord

from nextcord import Interaction
from nextcord.ext import commands
from typing import Final
from .setup_dir_path import SetupDirPath

#Allow access to modules from parent files.
SetupDirPath()


from src.utilities.data_manager import DataManager


COMMAND_NAME: Final[str] = "wing"

class Ping(commands.Cog):
    def __init__(self,bot: commands.Bot) -> None:
        """
        This class represents ping command.
        """
        self.bot: commands.bot = bot #Initialize the bot
        

    @nextcord.slash_command(name=COMMAND_NAME,description=DataManager().getCmdDescription(COMMAND_NAME))
    async def ping(self,ctx: Interaction) -> None:
        """
        The Ping command - respond to the user "Pong!" + the bot latency in milliseconds.
        """
        bot_latency: int = round(self.bot.latency * 1000)

        await ctx.send(f"Pong! {bot_latency}ms.")
        
        
    
def setup(bot: commands.Bot) -> None:
    #Setup the command
    bot.add_cog(Ping(bot))