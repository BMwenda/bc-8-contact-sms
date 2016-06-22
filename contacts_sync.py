import sys
sys.path.append('C:/Users/ALEX/Documents/GitHub/bc-8-contact-sms/contact-sms-env/Lib/site-packages')
from pyfirebase import Firebase
#import json
#import pdb; pdb.set_trace()

firebase = Firebase('https://contacts-7a958.firebaseio.com/')

ref = firebase.ref('contacts')

contacts = ref.get()

payload = {"id": "2", "first_name": "James", "last_name": "Andela", "phone_number": "+254729011229","is_sync": "0", "date_created": "2016-06-22 06:00:25", "user_id": "1"}

contacts = ref.push(payload)

root = firebase.ref()