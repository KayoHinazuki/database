from sqlalchemy import *
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

class User(declarative_base()):
    
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True)
    avatar = Column(String)
    user_id = Column(Integer)
    nickname = Column(String)
    is_fellow = Column(Boolean)
    is_friend = Column(Boolean)
    pv = Column(Integer)
    time_to_fellow = Column(DateTime)
    time_to_know = Column(DateTime)   

    def __repr__(self):
        return "%s(%r,%r,%r,%r,%r,%r,%r,%r,%r)" % (self.__tablename__,self.id,self.avatar,self.user_id,self.nickname,self.is_fellow,self.is_friend,self.pv,self.time_to_know,self.time_to_fellow)
 

