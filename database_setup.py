from sqlalchemy import Column, Integer, String

from sqlalchemy.schema import UniqueConstraint
#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for configuration
from sqlalchemy import create_engine

#create declarative_base instance
Base = declarative_base()

class Chores(Base):
    __tablename__ = 'chore'
    choreid = Column(Integer, primary_key=True)
    chore_title = Column(String(250), nullable=False)
    chore = Column(String(250), nullable=False)
   
    @property
    def serialize(self):
        return {
          self.chore_title : self.chore
        }

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///chores-collection.db')
Base.metadata.create_all(engine)
