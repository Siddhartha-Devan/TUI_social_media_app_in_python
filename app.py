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
        print("Suggested for ", self.name, '...')
        matching_profiles = []
        for user in all_users:
            if user != self.name:
                matching_index = 0

                # if user_data_base[user]['details'][0][3:5] == self.dob[3:5]:
                #     matching_index+=1
                # else:pass

                if  user_data_base[user]['details'][1] == self.age:
                    matching_index+=1
                else: pass

                if user_data_base[user]['details'][2].lower() == self.location.lower():
                    matching_index+=1
                else: pass

                if user_data_base[user]['details'][3].lower() == self.occupation.lower():
                    matching_index+=1
                else: pass

                matching_profiles.append([matching_index, user])


        matching_profiles = sorted(matching_profiles)[::-1]

        for i in matching_profiles:
            if i[0] > 0:
                print('-- -- ', i[1], ' -- --', i[0])
        print("Some other users are:")
        for i in matching_profiles:
            if i[0] == 0:
               print('-- -- ', i[1], ' -- --')      
        
    def add_friend(self, user):
        all_users = list(user_data_base.keys())
        if user in all_users:
            self.friends.append(user)
            # user_data_base[self.name]['friends'].append(user)
            print(user, ' added to friends succesfully')
            print('These are', self.name, "'s",' friends') 
            for friend in self.friends:
                print('-- -- ', friend,' -- --')

        else:
            print('No such user exists... review the code')

    
    
sidd = User('Sidd', '7890', '07/10/2003', 21, 'Salem', 'Engineer')
kavin = User('Kavin', '6789', '24/05/2004', 20, 'Ramnad', 'Developer')
pravin = User('Pravin', '1234', '21/12/2003', 20, 'Namakkal', 'Designer')
sibi = User('Sibi', '2003', '04/12/2002', 21, 'Salem', 'Engineer')
vicky = User('Vicky', '4567', '25/05/2003', 21, 'Dharmapuri', 'Designer')
vettri = User('Vettri', '2222', '06/01/2003', 22, 'Erode', 'Student')
gokul = User('Gokul', '1111', '04/02/2003', 21,'Salem', 'Student')

# sidd.add_friend('Kavin')
kavin.add_friend('Gokul')
kavin.add_friend('Vettri')

sidd.suggest_friends()
kavin.suggest_friends()

print(sidd.password)
print(user_data_base)


with open(db_path, 'w') as file:
    json.dump(user_data_base, file, indent=4)
    file.close()

