from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

class Weibo(declarative_base()):
	
	__tablename__ ='weibo'

	id = Column(Integer,primary_key=True)
	weibo = Column(Text)
		