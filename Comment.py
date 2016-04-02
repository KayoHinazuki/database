from sqlalchemy import *
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

class Comment(declarative_base()):

    __tablename__ = 'comment'

    id = Column(Integer,primary_key=True)
    comment = Column(String)
    weibo_id = Column(Integer)
    user_id = Column(Integer)
    record_time = Column(DateTime)
    send_time = Column(DateTime)
    image = Column(String)
    is_retweet = Column(Boolean)

    def __repr__(self):
        return "%s(%r,%r,%r,%r,%r,%r,%r,%r)" % (self.__tablename__,self.id,self.comment,self.user_id,self.weibo_id,self.record_time,self.image,self.send_time,self.is_retweet)
