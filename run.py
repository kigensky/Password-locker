from user import User, Credentials 

def function():
    print("               ____                         _                                          ")
	print("              |  _ \                       | |                     _   __              ")
	print("              | |_) )  ____  ___   ___     | |       ______  ____ | | / /  ____  _ _   ")
	print("              |  __/  / _  |/ __  / __     | |      |  __  ||  __|| |/ /  / __ \| '_|  ")
	print("              | |    / (_| |\__ \ \__ \    | |____  | |__| || |__ | |\ \ |  ___/| |    ")
	print("              |_|    \_____| ___/  ___/    |_______||______||____||_| \_\ \____ |_|    ")
function()

def create_new_user(username,password):
    '''
    Function to create a new user with the username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()    

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
    
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()    