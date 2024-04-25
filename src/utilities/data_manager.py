import yaml
import json
import os

from typing import Union
from dotenv import load_dotenv


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
            with open(os.getenv("CONFIG_YAML_PATH"),"r") as config_file:    
                config_data: dict[str] = yaml.safe_load(config_file) #Get the 'config.yml' data

        except (FileNotFoundError, TypeError) as e:
            print("'config.yml' does not exist. please create the file or specify the correct path.\n")
            return None #Return 'None' if 'config.yml' file is not found
        
        return config_data #Return the 'config.yml' data



    def getData(self,data_group: str,data: str) ->Union[None,str,int,float,bool,list]:
        """
        Return data from the config.yaml.
        
        Return 'None' if data is not found
        """
        data_dict: dict["str"] | None = self.getConfigData().get(data_group) #Get data dictionary

        if data_dict is not None:
            return data_dict.get(data) #Return the data if found
        
        



    def getPath(self,file_name: str) -> str | None:
        """
        Return the path of a file.
        """
        try:
            paths: dict[str,str] = self.getConfigData().get("Paths") #Get the 'paths' dictionary
            file_path: str = paths.get(file_name) #Get the file path

            
        except AttributeError as e:
            print(f"An error occured while loading data config: {e}\n")
            return None #Return 'None' if getConfigData() did not return a dictionary.

        return file_path #Return the file path
    


    def getCmdDescription(self,cmd_name: str) ->str:
        """
        Get command descriptions.
        """
        path: str = self.getPath("command_descriptions")
        
        try:
            with open(path,"r") as cmd_descriptions_file:
                #Get the command description by the command's name
                cmd_description: str = json.load(cmd_descriptions_file).get(cmd_name)

        except (TypeError, FileNotFoundError) as e:
            print(f"An error occured while loading the JSON file: {e}")
            print(f"Please check if '{path}'is the correct path.\n")    
            return None #Return 'None' if json file could not be loaded.
            
        return cmd_description #Return the command's description