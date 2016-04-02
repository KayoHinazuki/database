from sqlalchemy import *
from sqlalchemy.orm import *
from get_config import get_config_str
from Weibo import Weibo

class DB(object):
    def __init__(self, path):
        self.engine = create_engine(get_config_str(path),echo=True)
        DBsession = sessionmaker(bind=self.engine)
        self.session = DBsession()

    def get_session(self):
        return self.session()
    
    def add(self,obj):
        return self.session.add(obj)

    def close(self):
        return self.session.close()

    def commit(self):
        return self.session.commit()            
        


if __name__ == '__main__':

    session = DB("database.cfg")

    new_user = Weibo(id=0,weibo_id=1)

    session.add(new_user)

    session.commit()

    session.close()