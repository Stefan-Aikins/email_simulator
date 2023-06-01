### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email(object):

    # Declare the class variable, with default value, for emails.
    has_been_read = False

    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    # first an email from hyperionDev team
    global Hyperion_email, Yvonne_email, British_gas_email
    Hyperion_email = Email(
        'student.support@hyperionDev.com', 'complete your tasks', '''
    Dear Student
    
    I hope this email finds you well
    
    Welldone for completing majority of your assigments
    You are currently ahead of your tasks and deadlines
    Please complete the remaining assignments as soon as possible.
    Kindly inform us as soon an you receive an invitation to an interview
    
    kind regards
    Student support
    
    ''')

    inbox.append(Hyperion_email)

    # An email from Yvonne Asantewaa
    Yvonne_email = Email('yvonne_asantewaa@hotmail.co.uk',
                         'Home setup deadline', '''
    Hello Stefan
    
    I hope all is well with you
    Please complete the tasks i have given you and present evidence
    I hope to hear from you soon
    
    thanks
    Yvonne
    ''')

    inbox.append(Yvonne_email)

    # Email from British Gas
    British_gas_email = Email(
        'britishgas.co.uk', 'Bill is ready', '''
    Dear Stefan
    
    Your next bill is ready to view
    Please send your payment as soon as possible
    We have a support scheme for people struggling
    with hight cost of living
    For more info pls visit our page
    
    kind regards
    Customer services
    ''')

    inbox.append(British_gas_email)

    # Render all emails unread status
    for email_obj in inbox:
        email_obj.has_been_read


# Call the function to populate the Inbox for further use in your program.
populate_inbox()


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    i = 1
    print('Inbox:')
    for subj in inbox:
        print(f'{i}. {subj.subject_line} (From: {subj.email_address})')
        i += 1


# Create a function which displays a selected email.
index = 0


def read_email(index):
    try:
        index = int(input('Select an email to read: '))
        print(f'''
        from: {inbox[index - 1].email_address}
        Subject: {inbox[index - 1].subject_line}

        {inbox[index - 1].email_content}
                ''')
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        inbox[index-1].mark_as_read()
    except ValueError:
        print('wrong selection, Please type a number')

    # --- Email Program --- #

    # User must selct an option from the menu by typing number
menu = True
while True:
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:
            # list email subjects to select from
            print(f'{list_emails()}\n')
            print(read_email(index))
        elif user_choice == 2:
            # view unread emails if it has not been read
            l = 1
            for mail in inbox:
                if mail.has_been_read is False:
                    print(f'{l}. {mail.subject_line}')
                    l += 1
                else:
                    pass
        elif user_choice == 3:
            # close the application and return to the main menu
            print('Goodbye!')
            break
        else:
            print("Oops - incorrect input.")
    except ValueError:
        print('wrong selection, Please enter a number')
