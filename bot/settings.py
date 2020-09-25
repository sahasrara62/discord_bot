from typing import Any

import os

# Loading the data from the project environment/.env into system
database_url = os.getenv('DATABASE_URL')
discord_token = os.getenv('DISCORD_TOKEN')


class Config:
    def __init__(self):
        pass

    @staticmethod
    def get_config():
        """
        provide a single object having all config details stored
        :return:dict having config details to the search, discord, database
        """
        bot_config = {
            "search": {

                "tld": "com",
                "lang": "en",
                "tbs": "0",
                "safe": "off",
                "num": 10,
                "start": 0,
                "stop": 5,
                "pause": 2.0,
                "country": "",
                "extra_params": None,
                "user_agent": None,
                "verify_ssl": True
            },
            "discord_bot": {
                "token": discord_token
            },
            "database": {
                "database_url": database_url
            }

        }
        return bot_config


# config dictionary
config = Config.get_config()
