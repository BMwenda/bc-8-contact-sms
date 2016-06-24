# bc-8-contact-sms

## Introduction

    * A utility that allows you to:
      * 1.Save your contacts.
      * 2.Search you contacts.
      * 3.Send one-way text messages to a contact of choice.
      * 4.Sync contacts on firebase.
    
    * Usage:
      * contacts_manage add -p <phonenumber> -n <name>...')
      * contacts_manage search <name>')
      * contacts_manage text <name> -m <messagebody>...')
      * contacts_manage sync -c')
      * contacts_manage retrieve -c')
      * contacts_manage (-i | --interactive)')
      * contacts_manage (-h | --help | --version)')
    
    * Options:
      * -i, --interactive  Interactive Mode')
      * -h, --help  Show this screen and exit.')
      * --version  Show version.')
    * type help for a list of commands.

##Installation and Setup

1. Install python
	* Download Python onto your computer by using the following links
		* **Windows** - [Python Downloads](https://www.python.org/downloads/windows/)
		* **Mac** - [Python for Mac OS X](https://www.python.org/downloads/mac-osx/)
		* **Ubuntu** - install python2.x and python2.x-dev packages
		* **Other systems** - see the [general download page](https://www.python.org/downloads/)

	* To ensure you have Python on your computer:
		* Open the Command Prompt
		* Type Python.
		* If you have Python installed, you should see a response that includes the version number.

2. Clone the repository to your local folder of your choice
	* Open Git Bash
	* Change the working directory on cmd to the location where you want your clone made
	* Type 'git clone ' and paste the URL [Repo Location](https://github.com/gatobualex/bc-8-contact-sms.git)
	*Press **Enter** to finish creating your cloned repository


3. Install the virtual environment
	* To install globally with pip type the command `$ pip install virtualenv`

4. Install required modules
	* Open the requirements.txt file and pip install the required modules using `pip install -r requirements.txt`

5. Run ThoughtBook app
	* On your console type in `python contacts_commands.py -i` to run the app interactively
