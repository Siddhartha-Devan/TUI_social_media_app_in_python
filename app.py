import json
list_of_users = []

db_path = r'C:\Users\Siddhartha Devan V\.spyder-py3\ZOHO\Social media app\users_db.json'

with open(db_path, 'r') as file:
    user_data_base = json.load(file)
    file.close()
# user_data_base = {}
print(type(user_data_base))

class User:
    def __init__(self, name,password, dob, age, location, occupation, friends_l= [], requests_l= [], new_user=True):
        self.name = name
        self.password = password
        self.dob = dob
        self.age = age
        self.location = location
        self.occupation = occupation
        self.friends = friends_l
        self.requests = requests_l
        
        if new_user:
            user_data_base[self.name] = {'password': self.password, 'details' : [self.dob, self.age, self.location, self.occupation], 'friends' : self.friends,'requests' : self.requests}
        # user_data_base[self.name] = [self.dob, self.age, self.location, self.occupation, self.friends, self.requests, self]
        # list_of_users[self.name] = self


    def suggest_friends(self):
        all_users = list(user_data_base.keys())
        

sidd = User('Sidd', '7890', '07/10/2003', 21, 'Salem', 'Engineer')
kavin = User('Kavin', '6789', '24/05/2004', 20, 'Ramnad', 'Developer')
pravin = User('Pravin', '1234', '21/12/2003', 20, 'Namakkal', 'Designer')
sidd.suggest_friends()

print(sidd.password)
print(user_data_base)


with open(db_path, 'w') as file:
    json.dump(user_data_base, file, indent=4)
    file.close()

