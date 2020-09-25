from .settings import config
from .database import UserQueries, insert_data
from .search import search_google
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from difflib import SequenceMatcher


search_config = config['search']
database_config = config['database']
discord_config = config['discord_bot']

_engine = create_engine('{}'.format(database_config['database_url']), echo=False)
__Session = sessionmaker(bind=_engine)

session = __Session()


def get_recent_query(user_id, msg=None):
    result = session.query(UserQueries.user_query).filter(UserQueries.user_id == str(user_id)).all()

    if not msg:
        if len(result) == 0:
            return False
        if len(result) >= 5:
            result = result[:5]

        for res in result:
            yield res[0]
    else:
        res = list(filter(lambda x: SequenceMatcher(None, msg, x[0]).ratio() > 0.4, result))
        res2 = list(filter(lambda x: msg in x[0], result))
        final_res = set(res + res2)

        for obj in final_res:
            yield obj[0]


def search_result(query, user_id):
    save_query = insert_data(user_id=user_id, query=query.strip(), sess=session)
    if save_query:
        print("search query is saved.")

    return search_google(query, **search_config)
