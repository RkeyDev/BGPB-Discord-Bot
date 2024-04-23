import yaml
import json
from dotenv import load_dotenv
import os

class DataManager:

    def __init__(self) -> None:
        """
        This class is used to load data from configuration files.
        """
        load_dotenv(".env") #Load enviroment variables


    def getConfigData(self) -> dict | None:
        """
        Get config.yml file
        """
        try:
            with open(os.getenv("config_yaml_path"),"r") as config_file:    
                config_data: dict[str] = yaml.safe_load(config_file) #Get the 'config.yml' data

        except FileNotFoundError as e:
            print("'config.yml' does not exist. please create the file or specify the correct path.")
            return None #Return 'None' if 'config.yml' file is not found
        
        return config_data #Return the 'config.yml' data



    def getPath(self,file_name: str) -> str | None:
        """
        Return the path of a file.
        """
        try:
            paths: dict[str,str] = self.getConfigData().get("paths") #Get the 'paths' dictionary
            file_path: str = paths.get(file_name) #Get the file path

            
        except AttributeError:
            return None #Return 'None' if getConfigData() did not return a dictionary.

        return file_path #Return the file path
    


    def getCmdDescription(self,cmd_name: str) ->str:
        """
        Get command descriptions.
        """
        path = self.getPath("command_descriptions")
        
        try:
            with open(path,"r") as cmd_descriptions_file:
                #Get the command description by the command's name
                cmd_description: str = json.load(cmd_descriptions_file).get(cmd_name)

        except (TypeError, FileNotFoundError) as e:
            print(f"An error occured while loading the JSON file: {e}")
            print(f"Please check if '{path}'\nis the correct path.")    
            return None #Return 'None' if json file could not be loaded.
            
        return cmd_description #Return the command's description
        

print(DataManager().getCmdDescription("ping"))