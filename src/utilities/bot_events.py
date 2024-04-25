from nextcord.ext import commands

class LoadBotEvents:
    def __init__(self,bot: commands.Bot) -> None:
        """
        Load all the bot events.
        """

        @bot.event
        async def on_ready() -> None:
            """
            This event is called when the bot is online.
            """ 
            print(f"Bot logged in as {bot.user}")
        