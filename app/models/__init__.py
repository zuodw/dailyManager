import sqlalchemy as sa
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib
import pyodbc
from app.models.models import Person


DRIVER = '{Microsoft Access Driver (*.mdb, *.accdb)}'
PASSWORD = r'ba7fa3c49bd914f16'
DATABASE = r'D:\code\python\dailyManager\hmi.accdb'

CONNECTION_STR = ('DRIVER=%s;PWD=%s;DBQ=%s' % (DRIVER, PASSWORD, DATABASE))
CONNECTION_URL = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(CONNECTION_STR)}"

engine = sa.create_engine(CONNECTION_URL, echo=False)
DBSession = sessionmaker(engine)
session = DBSession()

person = session.query(Person).filter(Person.SNo==25).one()
print(person.Problem)
