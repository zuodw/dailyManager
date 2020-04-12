from app.models import session
from app.models.models import Person


class PersonCtrl(object):
    def query_byName(self, username):
        person = session.query(Person).filter_by(Name=username)
        return person

    def query_byName_Last2Week(self, username):
        person = session.query(Person).filter_by(Name=username)[-14:]
        return person

