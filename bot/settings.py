



import os

database_url = os.getenv('DATABASE_URL')
discord_token = os.getenv('DISCORD_TOKEN')


class Config:
  @staticmethod
  def get_config():

    config = {
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
        "database_url":database_url
      }

      }
    return config

config = Config.get_config()