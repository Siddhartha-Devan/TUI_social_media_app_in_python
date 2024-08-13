class User:
    def __init__(self, name,password, dob, age, location, occupation, new_user=True):
        self.name = name
        self.password = password
        self.dob = dob
        self.age = age
        self.location = location
        self.occupation = occupation
        self.friends = []
        self.requests = []

        if new_user:
            self.updater()
        # if new_user:
        #     user_data_base[self.name] = {'password': self.password, 'details' : [self.dob, self.age, self.location, self.occupation], 'friends' : self.friends,'requests' : self.requests}
        # user_data_base[self.name] = [self.dob, self.age, self.location, self.occupation, self.friends, self.requests, self]
        # list_of_users[self.name] = self

    def updater(self):
        user_data_base[self.name] = {'password': self.password, 'details' : [self.dob, self.age, self.location, self.occupation], 'friends' : self.friends,'requests' : self.requests}
        

    def show_mutual_friends(self):
        all_users = list(user_data_base.keys())

        existing_friends = self.friends
        print("---- ", existing_friends)
        print('These are your mutual friends...')
        mutual_friends = set()
        for friend in existing_friends:
            mutual_friends_i = user_data_base[friend]['friends']
            # print(mutual_friends_i)
            for i in mutual_friends_i:
                mutual_friends.add(i)

        for mf in mutual_friends:
            print(mf)        

    def suggest_friends(self):
        all_users = list(user_data_base.keys())
        self.show_mutual_friends()
        print("Suggested for ", self.name, '...')
        matching_profiles = []
        for user in all_users:
            if user != self.name and user not in self.friends:
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
        # print(all_users)
        if user in all_users:
            print("existing f => ", self.friends)
            self.friends.append(user)
            
            # user_data_base[self.name]['friends'].append(user)
            print(user, ' added to friends succesfully')
            print('These are', self.name, "'s",' friends') 
            for friend in self.friends:
                print('-- -- ', friend,' -- --')

            self.updater()
            
        else:
            print('No such user exists... review the code')

    
    def send_request(self, user):
        all_users = list(user_data_base.keys())

        if user in all_users and user not in self.friends:
            if self.name not in user_data_base[user]['requests']:
                user_data_base[user]['requests'].append(self.name)
                print('request sent to ', user, ' from ', self.name)

            elif self.name in user_data_base[user]['requests']:
                print('pending request, wait for ', user, ' to accept your request')

    def accept_request(self, user):
        if user in self.requests:
            self.requests.remove(user)
            self.friends.append(user)
            self.updater()
            print('request from ', user, ' is accepted')
            print('the pending requests are ', self.requests)
            print('these are your friends -- ', self.friends)
        else:
            print('No pending request from ', user)

    def reject_request(self, user):
        if user in self.requests:
            self.requests.remove(user)
            self.updater()
            print('request from ', user, 'is rejected')
            print('the pending requests are ', self.requests)
            print('these are your friends -- ', self.friends)
        else:
            print('No pending request from ', user)

