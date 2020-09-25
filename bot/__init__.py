# custom modules
from .settings import config
from .database import UserQueries, insert_data
from .search import search_google

# python package modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from difflib import SequenceMatcher

# defining the configuration for each of module, search, database and discord

# search config ->  can change the result by  modifying the kwargs (filter)
search_config = config['search']

# contains database_url for connection
database_config = config['database']

# contains discord token details
discord_config = config['discord_bot']

# creating engine
_engine = create_engine('{}'.format(database_config['database_url']), echo=False)
__Session = sessionmaker(bind=_engine)

# creating a session object, which is being user by default in all queries
session = __Session()


def get_recent_query(user_id, msg=None):
    """
    Provide the result from user search history related to a msg (query)
    ie in server

     "!recent google" this message on discord server will give the user previously typed/search
     queries which has google inside it.

    :param user_id: user_id, discord server user information  who do the search
    :param msg: user query related to previous search !recent <query?
    :return: generator object having result or None

    """

    # getting all the user search history result
    result = session.query(UserQueries.user_query).filter(UserQueries.user_id == str(user_id)).all()

    # adding condition according to state of msg
    if not msg:
        if len(result) == 0:
            return False

        if len(result) >= 8:
            result = result[:8]

        """ returning only 8 recent search query, """
        return [res[0] for res in result]
        # for res in result:
        #     yield res[0]
    else:
        # usign sequencematcher to check the ratio upto which two strig matched, setting matched limit to 0.4
        res = list(filter(lambda x: SequenceMatcher(None, msg, x[0]).ratio() > 0.4, result))

        # in some case when one string is larger than other string then result vary, so just added a simple check
        res2 = list(filter(lambda x: msg in x[0], result))

        # showing only unique search result
        final_res = set(res + res2)

        # returning back the results
        return [obj[0] for obj in final_res]
        # for obj in final_res:
        #     yield obj[0]


def search_result(query, user_id):
    """
    search_result function will search the google and provide the result according to user query.

    :param query:  user searching string !google <string>
    :param user_id: discord server each user id
    :return: generator object having result
    """

    # storing the user query in database for making his search persistent
    save_query = insert_data(user_id=user_id, query=query.strip(), sess=session)

    if save_query:
        print("search query is saved.")
    # calling main search function with defined config, here in config we limit the search result to 5
    return search_google(query, **search_config)
