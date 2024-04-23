from nextcord import Interaction
import nextcord
from nextcord.ext import commands

from services.data_manager import DataManager

class Ping(commands.Cog):
    def __init__(self,bot: commands.Bot) -> None:
        """
        This class represents ping command.
        """
        self.bot: commands.bot = bot

    @nextcord.slash_command(name="ping",description=DataManager().getCmdDescription("ping"))
    async def ping(self,ctx: Interaction) -> None:
        """
        The Ping command - respond to the user "Pong!" and the bot latency in milliseconds.
        """
        bot_latency: int = round(self.bot.latency * 1000)

        await ctx.send(f"Pong! {bot_latency}ms.")
        
        
    
def setup(bot: commands.Bot) -> None:
    #Setup the command
    bot.add_cog(Ping(bot))