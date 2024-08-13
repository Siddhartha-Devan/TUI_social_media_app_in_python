import json
from user_module import User

list_of_users = []

db_path = r'C:\Users\Siddhartha Devan V\.spyder-py3\ZOHO\Social media app\users_db.json'

with open(db_path, 'r') as file:
    user_data_base = json.load(file)
    file.close()
# user_data_base = {}
print(type(user_data_base))




sidd = User('Sidd', '7890', '07/10/2003', 21, 'Salem', 'Engineer')
kavin = User('Kavin', '6789', '24/05/2004', 20, 'Ramnad', 'Developer')
pravin = User('Pravin', '1234', '21/12/2003', 20, 'Namakkal', 'Designer')
sibi = User('Sibi', '2003', '04/12/2002', 21, 'Salem', 'Engineer')
vicky = User('Vicky', '4567', '25/05/2003', 21, 'Dharmapuri', 'Designer')
vettri = User('Vettri', '2222', '06/01/2003', 22, 'Erode', 'Student')
gokul = User('Gokul', '1111', '04/02/2003', 21,'Salem', 'Student')

sidd.add_friend('Kavin')
kavin.add_friend('Gokul')
kavin.add_friend('Vettri')
vettri.add_friend('Kavin')


sibi.send_request('Vettri')
sibi.send_request('Vettri')
pravin.send_request('Vettri')

vettri.reject_request('Pravin')
vettri.accept_request('Sibi')

vettri.suggest_friends()
# print(sidd.password)
# print(user_data_base)




actions_list = ["login", "signup", "suggest_friends", "send_request","my_friends", "view_requests",
                 "accept_request", "reject_request", "done"]
def printer(actions_list):
    print("The below are the allowed functions:")
    for i in actions_list:
        print(i)


printer(actions_list)   
print("enter done to exit")
inp = input("Enter your action: ")

while inp != 'done':
    if inp == 'login':
        user_name = input("Enter your user_name:")
        password = input("Enter your password")

        # if user_data_base 


with open(db_path, 'w') as file:
    json.dump(user_data_base, file, indent=4)
    file.close()