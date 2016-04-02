from sqlalchemy import *
from sqlalchemy.orm import *
from get_config import get_config_str
from Weibo import Weibo




if __name__ == '__main__':
    engine = create_engine(get_config_str('database.cfg'),echo=True)

    DBSession = sessionmaker(bind=engine)
    
    session = DBSession()

    new_user = Weibo(id=0,weibo_id=1)

    session.add(new_user)

    session.commit()

    session.close()