import sys
sys.path.append('C:/Users/ALEX/Documents/GitHub/bc-8-contact-sms/contact-sms-env/Lib/site-packages')
from pyfirebase import Firebase

class ContactsSync(object):
    firebase = Firebase('https://contacts-7a958.firebaseio.com/')
    ref = firebase.ref('contacts')

    def __init__(self):
        pass

    def contacts_get(self):
        contacts = ContactsSync.ref.get()
        root = ContactsSync.firebase.ref()
        return contacts

    def contacts_push(self, list_contacts):
        #list_contacts is a collection of dictionaries
        for contact in list_contacts:
            payload = contact
            contacts = ContactsSync.ref.push(payload)

        root = ContactsSync.firebase.ref()
        return contacts