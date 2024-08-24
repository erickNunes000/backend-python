from src.infra.config import *
from src.infra.entities import *

"""
from sqlalchemy.ext.declarative import declarative_base
myBase = declarative_base()
"""

db_conn = DBConnectionHandler()
engine = db_conn.get_engine()

Base.metadata.create_all(engine)
