"""
This interactive command application utility uses docopt with the 
built in cmd module for contact management and sending SMSs.

Usage:
    contacts_manage add -p <phonenumber> -n <name>...
    contacts_manage search <name>
    contacts_manage text <name> -m <messagebody>...
    contacts_manage sync -c
    contacts_manage (-i | --interactive)
    contacts_manage (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --version  Show version.
"""
 
 
import sys
sys.path.append('C:\Users/ALEX/Documents/GitHub/bc-8-contact-sms/contact-sms-env/Lib/site-packages')
from sys import argv
import getpass
import cmd
from docopt import docopt, DocoptExit
from users_crud import UsersCrud
from contacts_crud import ContactsCrud
from messages_crud import MessagesCrud
from send_sms import SendSms
from contacts_sync import ContactsSync

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class ContactsManage (cmd.Cmd):
    intro = 'Tangamana \n'\
    + ''\
    + ' (type help for a list of commands.)'

    global user_id
    global user_name
    user_exists = False
    trials = 3

    while user_exists != True:
        username = raw_input("Username: ")
        password = getpass.getpass("Password: ")
        user_find = UsersCrud()
        if len(username) > 0 and len(password) > 0:
            user_present = user_find.find_user_by_username_password(username, password)
            if user_present != None:
                user_id = user_present.id
                user_name = user_present.first_name.title() + " " + user_present.last_name.title()
                user_exists = True
            else:
                trials -= 1
                print "Please input a valid username and password."
                print trials, " more attempts."
        else:
            print "Please input a valid username and password."
            continue
        
        if trials == 0:
            print "You have run out of attempts. \nThank you. Good Bye!"
            exit()
        else:
            continue

    prompt = '(contacts_manage) '
    file = None
    
    @docopt_cmd
    def do_add(self, arg):
        """Usage: add -p <phonenumber> -n <name>..."""

        #print(arg)
        #print(arg['-n'])
        #print(arg['-p'])
        #print(arg['<name>'])
        #print(arg['<phonenumber>'])
        id = 0
        is_sync = 0
        contact_new = ContactsCrud()
        if contact_new.create_contact(arg['<name>'][0], arg['<name>'][1], arg['<phonenumber>'], is_sync, user_id) == True:
            print(arg['<name>'][0] + " has been saved.")
        else:
            print("Contact " + arg['<name>'][0] + " failed to save.")
        

    @docopt_cmd
    def do_search(self, arg):
        """Usage: search <name>"""

        #print(arg)
        #print(arg['<name>'])
        contacts_find = ContactsCrud()
        search_result = contacts_find.find_contact_by_keyword((arg['<name>']).title())
        if len(search_result) == 0:
            print((arg['<name>']).title() + " does not exist.")
        elif len(search_result) == 1:
            print("Name: " + search_result[0].first_name + " " + search_result[0].last_name + " Phone number: " + search_result[0].phone_number)
        else:
            str_response = "Which " + (arg['<name>']).title() + "? \n"
            count = 0
            for contact in search_result:
                count += 1
                str_response += "[" + str(count) + "] " + contact.first_name + " "
            else:
                str_response += "i.e " + search_result[0].first_name + " " + search_result[0].last_name + ", " + search_result[1].first_name + " " + search_result[1].last_name + " etc"
            print(str_response)
            
            
    @docopt_cmd
    def do_text(self, arg):
        """Usage: text <name> -m <messagebody>..."""
        
        #print(arg)
        #print(arg['<name>'])
        #print(arg['-m'])
        #print(arg['<messagebody>'])

        #Get name
        #Use name to obtain number
        #Invoke SendSms to send text
        #Save message body to database

        sms_new = SendSms()
        contacts_find = ContactsCrud()
        search_result = contacts_find.find_contact_by_keyword((arg['<name>']).title())
        if len(search_result) == 0:
            print((arg['<name>']).title() + " does not exist.")
        elif len(search_result) == 1:
            sms_new.send_sms(search_result[0].phone_number, " ".join(arg['<messagebody>']), user_name)
        else:
            prompt = 'Recipient Selection> '
            str_response = "There exists multiple individuals, \nwith the name " + (arg['<name>']).title()
            str_response += "\nPlease provide the desired recipient. \n"
            count = 0
            for contact in search_result:
                count += 1
                str_response += "[" + str(count) + "] " + contact.first_name + " " + contact.last_name + "\n"
            print(str_response)
            destination = raw_input(prompt)
            single_result = contacts_find.find_contact_by_name(str(destination).split())
            sms_new.send_sms(single_result[0].phone_number, " ".join(arg['<messagebody>']), str(user_name))
    
    @docopt_cmd
    def do_sync(self, arg):
        """Usage: sync -c"""
        
        #print(arg)
        #print(arg['-c'])

        #Get list of contacts
        #Pass list of contacts to firebase handler class

        contacts_list = ContactsCrud()
        contacts_sync = ContactsSync()
        contacts_to_push = contacts_list.find_contact_to_sync()
        contacts_sync_result = contacts_sync.contacts_push(contacts_to_push)
        contacts_list.update_contact_post_sync(contacts_to_push)
        print(contacts_sync_result)
    
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank You. Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ContactsManage().cmdloop()

print(opt)