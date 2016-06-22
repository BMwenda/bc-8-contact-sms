from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from database import Contact

class ContactsCrud(object):
	engine = create_engine('sqlite:///contacts_manage.sqlite', echo = False)
	
	# create a Session
	Session = sessionmaker(bind=engine)
	session = Session()
	
	
	def __init__(self):
        #Use pass since NameError: name 'first_name' is not defined error
        #when you pass values in the function and 
        #use self.property = property_value in init
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

	def update_contact(self, id, first_name, last_name, phone_number, is_sync, user_id):
		contacts = ContactsCrud.session.query(Contact).filter(Contact.id==id).all()
		contacts.first_name = first_name
		contacts.last_name = last_name
		contacts.is_sync = is_sync
		contacts.user_id = user_id
		ContactsCrud.session.add(contacts)
		ContactsCrud.session.commit()
		return True
		
	def delete_contact(self, id):
		contacts = ContactsCrud.session.query(Contact).filter(Contact.id==id).all()
		ContactsCrud.session.delete(contacts)
		ContactsCrud.session.commit()
		return True