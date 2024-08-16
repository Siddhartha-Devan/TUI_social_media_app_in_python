import json
from user_module import User
from user_module import user_db_obj
print(user_db_obj.user_data_base)
list_of_users = []

# db_path = r'C:\Users\Siddhartha Devan V\.spyder-py3\ZOHO\Social media app\users_db.json'

# with open(db_path, 'r') as file:
#     user_data_base = json.load(file)
#     file.close()
# # user_data_base = {}
# print(type(user_data_base))

# user_db = UserDbManager(db_path)





# Used for initial database setup...


# sidd = User('Sidd', '7890', '07/10/2003', 21, 'Salem', 'Engineer', new_user=False)
# kavin = User('Kavin', '6789', '24/05/2004', 20, 'Ramnad', 'Developer', new_user=False)
# pravin = User('Pravin', '1234', '21/12/2003', 20, 'Namakkal', 'Designer', new_user=False)
# sibi = User('Sibi', '2003', '04/12/2002', 21, 'Salem', 'Engineer', new_user=False)
# vicky = User('Vicky', '4567', '25/05/2003', 21, 'Dharmapuri', 'Designer', new_user=False)
# vettri = User('Vettri', '2222', '06/01/2003', 22, 'Erode', 'Student', new_user=False)
# gokul = User('Gokul', '1111', '04/02/2003', 21,'Salem', 'Student', new_user=False)

# sidd.add_friend('Kavin')
# kavin.add_friend('Gokul')
# kavin.add_friend('Vettri')
# vettri.add_friend('Kavin')


# sibi.send_request('Vettri')
# sibi.send_request('Vettri')
# pravin.send_request('Vettri')

# vettri.reject_request('Pravin')
# vettri.accept_request('Sibi')

# vettri.suggest_friends()
# print(sidd.password)
# print(user_data_base)




actions_list = ["login", "signup", "suggest_friends", "send_request","my_friends", "view_requests",
                 "accept_request", "reject_request", "done"]

def printer(actions_list):
    print("The below are the allowed functions:")
    for i in actions_list:
        print(i)


current_user = None

printer(actions_list)   
print("enter done to exit")
inp = input("Enter your action: ")

def user_checker(current_user):
    if current_user == None:
        print("Login or signup first...")
        return False
    else:
        return True

while inp != 'done':
    if inp == 'login':
        user_name = input("Enter your user_name: ")
        password = input("Enter your password: ")

        log_data = user_db_obj.retrieve_data_for_login(user_name, password)
        
        current_user = User(user_name, log_data['password'], log_data['details'][0], log_data['details'][1], log_data['details'][2], log_data['details'][3], friends_l= log_data['friends'], requests_l=log_data['requests'], new_user=False)
        print(log_data)

        current_user.suggest_friends()
    
    if inp == 'signup':
        print("Enter your deatils to create account:")
        print("Note: there shouldn't be any spaces in username or password")
        user_name_password = input("Enter your username and password: ")
        user_name, password = user_name_password.split(" ")

        new_user_details = input('Enter your details in the following order-> dd/mm/yyyy age location occupation: ' )
        new_user_details = new_user_details.split(" ")

        current_user = User(user_name, password, new_user_details[0], new_user_details[1], new_user_details[2], new_user_details[3])
        print("New User Created... Welcome", user_name)


    if inp == 'suggest_friends':
        if user_checker(current_user):
            current_user.suggest_friends()
    
    if inp == 'my_friends':
        if user_checker(current_user):
            current_user.my_friends()
        
    if inp == 'view_requests':
        if user_checker(current_user):
            current_user.my_requests()

    if inp == 'send_request':
        if user_checker(current_user):
            user = input("Enter the name of the user whom you want to send the request to: ")
            current_user.send_request(user)

    if inp == 'accept_request':
        if user_checker(current_user):
            user = input("Enter the name of the user whose request you wanna accept: ")
            current_user.accept_request(user)

    if inp == 'reject_request':
        if user_checker(current_user):
            user = input("Enter the name of the user whose request you wanna reject: ")
            current_user.reject_request(user)

    printer(actions_list)
    inp = input("Enter your action: ")

if inp == 'done':
    if user_checker(current_user):
        current_user.close_app()
        

        














# with open(db_path, 'w') as file:
#     json.dump(user_data_base, file, indent=4)
#     file.close()