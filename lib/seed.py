# seed.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Hospital, Patient, Transport


engine = create_engine('sqlite:///emerg.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# session.query(Hospital).delete()
# session.query(Patient).delete()
# session.query(Transport).delete()

