import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Contact

engine = create_engine('sqlite:///contacts_manage.sqlite', echo = True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

#Create a contact
new_contact = Contact(self.first_name, self.last_name, self.phone_number, self.is_sync, self.user_id)

# Add the record to the session object
session.add(new_contact)
# commit the record the database
session.commit()