# discord_bot


Discord_discord bot is a simple discord bot, which is deployed on heroku cloud environment.

discord_bot has following functionality

1. It reply ***hey*** to user ***hi***
2. Provide google search result (top 5)  by using 
    > **!google search_query**
3. Provide user recent search result for a query by using
    > **!recent query**
                                                             >
                                                             >


### How to Add discord_bot to your server

**bot details**
> discord_bot url = [discord_bot](https://discord.com/api/oauth2/authorize?client_id=758260433341251605&permissions=271969376&scope=bot)
> discord_bot name = ***prashant_bot***
>
>
### steps to add bot to your existing discord server

1. copy the discord bot [url](https://discord.com/api/oauth2/authorize?client_id=758260433341251605&permissions=271969376&scope=bot)

> `https://discord.com/api/oauth2/authorize?client_id=758260433341251605&permissions=271969376&scope=bot`
2. login to your discord account
3. paste the copied url in browser
4. select the exesting server where you want to add bot, authorise the permissions
5. go back to your server and see in the right side prashant_bot server is online

## how to run mannully

1. copy the codebase
2. in main directory, create a file `.env`, set the environment variable
3. add `DATABSE_URL` and `DISCORD_TOKEN`
4. run the command to run server `python app.py`

##### example of .env file

    DATABASE_URL="postgresql://<username>:<password>@<host_url>:<port>/databasename
    DISCORD_TOKEN="ELKJQWEIOJOWIEIOQWMQWEOIQWEUQOIEJUQWEOI"

### How to create tables through python 

1. In terminal/Konsole open `discord_bot` drirectory
2. open python shell ( first install all requirements)
3. in python shell run following commands

    a.  `from bot import _engine as engine`  
    b.   `from bot.database import Base`   
    c.  `Base.metadata.create_all(engine)`
 

#### contact
  email: `uchiha.rana62@gmail.com`