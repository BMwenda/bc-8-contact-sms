import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'contact-sms-env\Lib\site-packages'))
import hashlib
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from database import User

class UsersCrud(object):
    engine = create_engine('sqlite:///contacts_manage.sqlite', echo = False)
    
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def __init__(self):
        pass
    
    def create_user(self, first_name, last_name, phone_number, username, password):
        #Create a user
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()
        new_user = User(first_name, last_name, phone_number, username, password)
        # Add the record to the session object
        UsersCrud.session.add(new_user)
        # commit the record the database
        UsersCrud.session.commit()
        return True
    
    def find_user_all(self):
        users = UsersCrud.session.query(User).all()
        return users
        
    def find_user_by_id(self, search_id):
        users = UsersCrud.session.query(User).filter(User.id==search_id).all()
        return users
    
    def find_user_by_username_password(self, username, password):
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()
        users = UsersCrud.session.query(User).filter(and_(User.username==username, User.password==password)).first()
        return users

    def update_user(self, first_name, last_name, username, password):
        hash_object = hashlib.md5(password.encode())
        password = hash_object.hexdigest()

        users = UsersCrud.session.query(User).filter(User.id==id).all()
        users.first_name = first_name
        users.last_name = last_name
        users.username = username
        users.password = password
        UsersCrud.session.add(users)
        UsersCrud.session.commit()
        return True

    def delete_user(self, id):
        users = UsersCrud.session.query(User).filter(User.id==id).all()
        UsersCrud.session.delete(users)
        UsersCrud.session.commit()
        return True