class Profile:
    def __init__(self, thisName, thisAge, thisBirthday, thisHobby):
        self.name = thisName
        self.age = thisAge
        self.birthday = thisBirthday
        self.hobby = thisHobby
        
            

#Class ends

user1 = Profile("Sophia", 18, "February 7", "Reading Books")
user2 = Profile("Kevin", 17, "December 5", "Gaming")
user3 = Profile("Sanniya", 17, "November 1", "Gaming")
user4 = Profile("Herman", 18, "July 17", "Basketball")

userList = [user1, user2, user3, user4]

for user in userList:
    print(user.name, user.age, user.birthday, user.hobby)