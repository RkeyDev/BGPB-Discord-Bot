from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from typing import Final

from .setup_dir_path import SetupDirPath

#Allow access to modules from parent files.
SetupDirPath()


from src.utilities.data_manager import DataManager
from src.utilities.weather_api import WeatherApi


COMMAND_NAME: Final[str] = "weather"


class Weather(commands.Cog):
    def __init__(self,bot: commands.Bot) -> None:
        """
        This class represents the Weather command.
        """
        self.bot: commands.bot = bot #Initialize the bot


    @nextcord.slash_command(name=COMMAND_NAME,description=DataManager().getCmdDescription(COMMAND_NAME))
    async def command(self,ctx: Interaction,city: str) -> None:
        """
        The Weather command - show the weather of a city.
        """
        weather_api = WeatherApi() #Load the weather API
        weather_details = weather_api.getWeatherDetails(city) #Get the weather details of a city

        #Send the temprature and the weather description
        await ctx.send(
            f"Weather in {city}:\nTemprature: {weather_details[0]}°C {weather_details[1]}"
                       )

        

def setup(bot: commands.Bot) -> None:
    #Setup the command
    bot.add_cog(Weather(bot))


