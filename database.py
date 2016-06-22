import sys
sys.path.append('C:\Users/ALEX/Documents/GitHub/bc-8-contact-sms/contact-sms-env/Lib/site-packages')
from sqlalchemy import create_engine, ForeignKey, func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


# Create a connection to a SQLite on-disk database "data.sqlite"
engine = create_engine('sqlite:///contacts_manage.sqlite', echo = False)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password = Column(String)
    date_created = Column(DateTime, default=func.now())
    
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name.upper()
        self.last_name = last_name.upper()
        self.username = username
        self.password = password
        self.date_created = None
       
    def __repr__(self):
        return "<Message('%s', '%s', '%s')>" % (self.first_name, self.last_name, self.username)
 
        
class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    is_sync = Column(Integer)
    date_created = Column(DateTime, default=func.now())
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref("contacts", order_by=id))
    
    def __init__(self, first_name, last_name, phone_number, is_sync, user_id):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.phone_number = phone_number
        self.is_sync = is_sync
        self.date_created = None
        self.user_id = user_id
        
    def __repr__(self):
        return "<Contact('%s', '%s', '%s', '%i')>" % (self.first_name, self.last_name, self.phone_number, self.is_sync)


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    source = Column(String)
    message_body = Column(String)
    date_sent = Column(DateTime, default=func.now())
    
    recipient_id = Column(Integer, ForeignKey("contacts.id"))
    recipient = relationship("Contact", backref=backref("messages", order_by=id))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref("messages", order_by=id))
    
    def __init__(self, source, recipient_id, message_body, user_id):
        self.source = source
        self.recipient_id = recipient_id
        self.message_body = message_body
        self.date_sent = None
        self.user_id = user_id
    
    def __repr__(self):
        return "<Message('%s', '%i', '%s', '%s', '%i')>" % (self.source, self.recipient, self.message_body, self.date_sent, self.user_id)
    

# create tables
Base.metadata.create_all(engine)