import sys
sys.path.append('C:\Users/ALEX/Documents/GitHub/bc-8-contact-sms/contact-sms-env/Lib/site-packages')
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from database import Message

class MessagesCrud(object):
    engine = create_engine('sqlite:///contacts_manage.sqlite', echo = False)
    
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    
    def __init__(self):
        #Use pass since NameError: name 'first_name' is not defined error
        #when you pass values in the function and 
        #use self.property = property_value in init
        pass
    
    def create_message(self, source, recipient_id, message_body, user_id):
        #Create a message
        new_message = Message(source, recipient_id, message_body, user_id)
        # Add the record to the session object
        MessagesCrud.session.add(new_message)
        # commit the record the database
        MessagesCrud.session.commit()
        return True
    
    def find_message_all(self):
        messages = MessagesCrud.session.query(Message).all()
        return messages
        
    def find_message_by_id(self, search_id):
        messages = MessagesCrud.session.query(Message).filter(message.id==search_id).all()
        return messages
        
    def find_message_by_recipient(self, recipient_id):
        messages = MessagesCrud.session.query(Message).filter(message.recipient_id==recipient_id).all()
        return messages
    
    def find_message_by_content(self, search_keywords):
        messages = MessagesCrud.session.query(Message).filter(message.message_body.like("%" + search_keywords + "%")).all()
        return messages
        
    def update_message(self, id, source, recipient_id, message_body, user_id):
        messages = MessagesCrud.session.query(Message).filter(message.id==id).all()
        messages.source = source
        messages.recipient_id = recipient_id
        messages.message_body = message_body
        messages.user_id = user_id
        MessagesCrud.session.add(messages)
        MessagesCrud.session.commit()
        return True
        
    def delete_message(self, id):
        messages = MessagesCrud.session.query(Message).filter(message.id==id).all()
        MessagesCrud.session.delete(messages)
        MessagesCrud.session.commit()
        return True