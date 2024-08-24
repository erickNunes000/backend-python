from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeUser:
    """fake user repository"""

    @classmethod
    def insert_user(cls):
        try:
            with DBConnectionHandler() as db_connection:
                new_user = Users(name="erico", password="1234")
                db_connection.session.add(new_user)
                db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
