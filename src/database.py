from sqlalchemy import create_engine
from .models import *

engine = create_engine('sqlite:///db.sqlite3')
