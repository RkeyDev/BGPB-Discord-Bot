import os

from nextcord.ext import commands
from utilities.bot_events import LoadBotEvents

from dotenv import load_dotenv


bot: commands.Bot = commands.Bot() #Create the bot object

def loadCommands() -> None:
    """
    Load all the commands (cogs).
    """
    for filename in os.listdir("src/cogs"):
        if filename.endswith(".py") and filename != "setup_dir_path.py":
            bot.load_extension(f"cogs.{filename[:-3]}") 
        

def main() -> None:
    """
    The main method.
    """

    #Load events and commands
    LoadBotEvents(bot)
    loadCommands()

    load_dotenv(".evn") #Load enviroment variables
    
    #Run the bot
    bot.run(os.getenv("BOT_TOKEN")) 



#The starting point of the program
if __name__ == "__main__":
    main()