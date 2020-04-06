from app.models import session
from app.models.models import Person


class PersonCtrl(object):
    def query_byName(self, username):
        person = session.query(Person).filter_by(Name=username)
        return person

