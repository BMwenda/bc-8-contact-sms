import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'contact-sms-env\Lib\site-packages'))
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from database import Contact

class ContactsCrud(object):
    engine = create_engine('sqlite:///contacts_manage.sqlite', echo = False)
    
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    def __init__(self):
        pass
    
    def create_contact(self, first_name, last_name, phone_number, is_sync, user_id):
        #Create a contact
        new_contact = Contact(first_name, last_name, phone_number, is_sync, user_id)
        # Add the record to the session object
        ContactsCrud.session.add(new_contact)
        # commit the record the database
        ContactsCrud.session.commit()
        return True
    
    def find_contact_all(self):
        contacts = ContactsCrud.session.query(Contact).all()
        return contacts
        
    def find_contact_by_id(self, search_id):
        contacts = ContactsCrud.session.query(Contact).filter(Contact.id==search_id).all()
        return contacts
    
    def find_contact_by_keyword(self, search_name):
        contacts = ContactsCrud.session.query(Contact).filter(or_(Contact.first_name.like("%" + search_name + "%"), Contact.last_name.like("%" + search_name + "%"))).all()
        return contacts
    
    def find_contact_by_name(self, list_names):
        contacts = ContactsCrud.session.query(Contact).filter(and_(Contact.first_name==list_names[0], Contact.last_name==list_names[1])).all()
        return contacts

    def find_contact_to_sync(self):
        contacts = ContactsCrud.session.query(Contact).filter(Contact.is_sync==0).all()
        list_contacts = []
        for contact in contacts:
            #Update is_sync flag
            contact.is_sync = 1

            dictionary_contact = {}
            dictionary_contact['id'] = contact.id
            dictionary_contact['first_name'] = contact.first_name
            dictionary_contact['last_name'] = contact.last_name
            dictionary_contact['phone_number'] = contact.phone_number
            dictionary_contact['is_sync'] = contact.is_sync
            dictionary_contact['date_created'] = str(contact.date_created)
            dictionary_contact['user_id'] = contact.user_id
            list_contacts.append(dictionary_contact)

        return list_contacts

    def update_contact(self, id, first_name, last_name, phone_number, is_sync, user_id):
        contacts = ContactsCrud.session.query(Contact).filter(Contact.id==id).all()
        contacts.first_name = first_name
        contacts.last_name = last_name
        contacts.is_sync = is_sync
        contacts.user_id = user_id
        ContactsCrud.session.add(contacts)
        ContactsCrud.session.commit()
        return True

    def update_contact_post_sync(self, list_contact):
        for contact in list_contact:
            with ContactsCrud.session.no_autoflush:
                ContactsCrud.session.query(Contact).filter(Contact.id==contact['id']).update({"is_sync": 1})
                ContactsCrud.session.commit()
        return True

    def delete_contact(self, id):
        contacts = ContactsCrud.session.query(Contact).filter(Contact.id==id).all()
        ContactsCrud.session.delete(contacts)
        ContactsCrud.session.commit()
        return True