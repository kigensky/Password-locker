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