from nextcord import Interaction
import nextcord
from nextcord.ext import commands

from utilities.data_manager import DataManager # type: ignore
from typing import Final

from project_init import *


COMMAND_NAME: Final[str] = "CommandName"

class CommandName(commands.Cog):
    def __init__(self,bot: commands.Bot) -> None:
        """
        This class represents the CommandName command.
        """
        self.bot: commands.bot = bot #Initialize the bot

    @nextcord.slash_command(name=COMMAND_NAME,description=DataManager().getCmdDescription(COMMAND_NAME))
    async def command(self,ctx: Interaction) -> None:
        """
        The CommandName command - Command description.
        """

def setup(bot: commands.Bot) -> None:
    #Setup the command
    bot.add_cog(CommandName(bot))
