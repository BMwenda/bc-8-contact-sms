"""
This interactive command application utility uses docopt with the 
built in cmd module for contact management and sending SMSs.

Usage:
    contacts_manage add -n <name> -p <phonenumber>
    contacts_manage search <name>
	contacts_manage text <name> -m <>
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
import cmd
from docopt import docopt, DocoptExit


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
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(contacts_manage) '
    file = None
	
    @docopt_cmd
    def do_add(self, arg):
        """Usage: add -n <name> -p <phonenumber>"""
        """Ask Wangari for example on splitting <name>"""

        print(arg)
        print(arg['-n'])
        print(arg['-p'])
        print(arg['<name>'])
        print(arg['<phonenumber>'])

    @docopt_cmd
    def do_search(self, arg):
        """Usage: search <name>"""

        print(arg)
        print(arg['<name>'])

	@docopt_cmd
	def do_text(self, arg):
		"""Usage: text <name> -m <messagebody>"""
		
		print(arg)
        print(arg['<name>'])
        print(arg['-m'])
        print(arg['<messagebody>'])
	
	@docopt_cmd
	def do_sync(self, arg):
		"""Usage: sync -c"""
		
		print(arg)
        print(arg['-c'])
	
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank You. Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ContactsManage().cmdloop()

print(opt)