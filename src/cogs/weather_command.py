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
    data_manager: DataManager = DataManager() #Create data manager object

    def __init__(self,bot: commands.Bot) -> None:
        """
        This class represents the Weather command.
        """
        self.bot: commands.bot = bot #Initialize the bot
        

    @nextcord.slash_command(name=COMMAND_NAME,description=data_manager.getJsonData(COMMAND_NAME))
    async def command(self,ctx: Interaction,city: str) -> None:
        """
        The Weather command - show the weather of a city.
        """
        city: str = city.capitalize()
        try:
            weather_api = WeatherApi() #Load the weather API
            weather_details = weather_api.getWeatherDetails(city) #Get the weather details of a certain city
            
            temp, weather_description = weather_details
            weather_emoji = weather_api.getWeatherEmoji(weather_description)

            #Send the temprature and the weather description
            await ctx.send(
                f"Weather in {city}:\nTemprature: {temp}°C {weather_description} {weather_emoji}"
                        )
            
        except KeyError as e:
            #Send a message if the city is not found
            await ctx.send(f"{city} is not a city on this planet. Please try a different city.")
            

        

def setup(bot: commands.Bot) -> None:
    #Setup the command
    bot.add_cog(Weather(bot))


