from app.models import session
from app.models.models import Project


class ProjectCtrl(object):
    def query_bySNo(self, SNo):
        project = session.query(Project).filter_by(SNo=SNo).first()
        return project

