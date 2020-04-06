import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Project(Base):
    __tablename__ = 'ProjectsDetailStateTable'

    SNo = sa.Column(sa.Integer(), primary_key=True)
    ProjectName = sa.Column(sa.Text(), nullable=False)
    SubProjectName = sa.Column(sa.Text(), nullable=False)
    PLA_PD_H = sa.Column(sa.Integer(), nullable=True)
    PLA_PDR_H = sa.Column(sa.Integer(), nullable=True)
    PLA_MK_H = sa.Column(sa.Integer(), nullable=True)
    PLA_MKR_H = sa.Column(sa.Integer(), nullable=True)
    PLA_CT_H = sa.Column(sa.Integer(), nullable=True)
    PLA_CTR_H = sa.Column(sa.Integer(), nullable=True)
    PLA_IT_H = sa.Column(sa.Integer(), nullable=True)
    PLA_ITR_H = sa.Column(sa.Integer(), nullable=True)
    PLA_Other_H = sa.Column(sa.Integer(), nullable=True)
    ExpectedStartDate = sa.Column(sa.Integer(), nullable=False)
    ExpectedEndDate = sa.Column(sa.Integer(), nullable=False)
    ActuallyStartDate = sa.Column(sa.Integer(), nullable=True)
    ActuallyEndDate = sa.Column(sa.Integer(), nullable=True)
    SchduleState = sa.Column(sa.Integer(), nullable=False)
    UpdateMemo = sa.Column(sa.Text(), nullable=True)
    UpdateTimeStamp = sa.Column(sa.Integer(), nullable=False)


class Person(Base):
    __tablename__ = 'PersonDailyDataTable'

    SNo = sa.Column(sa.Integer(), primary_key=True)
    UpdateDate = sa.Column(sa.Date(), nullable=False)
    Name = sa.Column(sa.Text(), nullable=False)
    ProjectNO = sa.Column(sa.Integer(), nullable=False)
    SubPjStage = sa.Column(sa.Text(), nullable=False)
    IsExpectedWork = sa.Column(sa.Text(), nullable=False)
    ActullyWorkContent = sa.Column(sa.Text(), nullable=False)
    WorkState = sa.Column(sa.Text(), nullable=False)
    Risk = sa.Column(sa.Text(), nullable=False)
    TommorwPlan = sa.Column(sa.Text(), nullable=False)
    Problem = sa.Column(sa.Text(), nullable=False)
    Hours = sa.Column(sa.Integer(), nullable=False)
    SubProjName = sa.Column(sa.Text(), nullable=False)


class User(Base):
    __tablename__ = 'User'

    ID = sa.Column(sa.Integer(), primary_key=True)
    Name = sa.Column(sa.Text(), nullable=False)
    Password = sa.Column(sa.Text(), nullable=False)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.ID

    def get_imgpath(self):
        return 'default.png'

    def __repr__(self):
        return'username:%s, password:%s' %(self.username, self.password)

