from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
import datetime


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserQueries(Base):

    __tablename__ = "discord_history"
    __table_args__ = {"schema": "public"}

    id = Column(Integer ,primary_key=True, nullable=False)
    user_id = Column(String(100), nullable=False)
    user_query = Column(String(100), nullable=False)
    query_time =  Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, user_id, user_query):
        self.user_id = user_id
        self.user_query = user_query


    def __repr__(self):
        return '<UserModel model {}>'.format(self.id)


def insert_data(user_id=None, query=None, sess=None):
    if not sess:
        return False
    if not user_id:
        return False
    if not query:
        return False
    try:
        obj = UserQueries(user_id, query)
        sess.add(obj)
        sess.commit()
        sess.close()
        return True
    except:
        sess.rollback()
        sess.close()
    finally:
        sess.close()
    return False
