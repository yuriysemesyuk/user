class User:
    def __init__(self, first_name, last_name, age=None, number_phone=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.number_phone = number_phone
        self.email = email

    def descripe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greeting_user(self):
        print(self.first_name)
        print(self.last_name)

user = User("Yuriy", "Semesyuk")

User.descripe_user(user)