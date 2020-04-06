from app.models.models import User
from app.models import session


class UserCtrl(object):
    def query(self, Name, Password):
        user = session.query(User).filter_by(Name=Name, Password=Password).first()
        return user

    def query_byId(self, ID):
        user = session.query(User).filter_by(ID=ID).first()
        return user

    def query_byName(self, Name):
        user = session.query(User).filter_by(Name=Name).first()
        return user

