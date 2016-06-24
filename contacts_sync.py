import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'contact-sms-env\Lib\site-packages'))
from pyfirebase import Firebase

class ContactsSync(object):
    firebase = Firebase('https://contacts-7a958.firebaseio.com/')

    def __init__(self):
        pass

    def contacts_get(self, user_name, phone_number):
        ref = ContactsSync.firebase.ref('contacts')
        contacts = ref.get()
        root = ContactsSync.firebase.ref()
        return contacts

    def contacts_push(self, list_contacts, user_name, phone_number):
        ref = ContactsSync.firebase.ref('contacts')
        #list_contacts is a collection of dictionaries
        for contact in list_contacts:
            payload = contact
            contacts = ref.push(payload)

        root = ContactsSync.firebase.ref()
        return contacts