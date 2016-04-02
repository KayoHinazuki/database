from sqlalchemy import *
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

class Weibo(declarative_base()):
    
    __tablename__ ='weibo'

    id = Column(Integer,primary_key=True)
    weibo = Column(Text)
    user_id = Column(Integer)
    weibo_id = Column(Integer)
    url = Column(String)
    images=Column(Text)
    time = Column(TIMESTAMP(timezone=True))

    def __repr__(self):
        return "%s(%r,%r,%r,%r,%r%r%r)" % (self.__tablename__,self.id,self.weibo,self.user_id,self.weibo_id,self.url,self.images,self.time)
