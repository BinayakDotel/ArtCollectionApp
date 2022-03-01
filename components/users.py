class User:
    __instance = None
   
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if User.__instance == None:
            User()
        return User.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if User.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            User.__instance = self
            
            self.id= 0
            self.full_name= "default"
            self.email= "default"
            self.password= "default"
            self.phone_number= "9841966784"
            self.role= "user"

    def set_id(self, id):
        self.id= id

    def set_name(self, name):
        self.full_name= name

    def set_email(self, email):
        self.email= id

    def set_phone_number(self, phone_number):
        self.phone_number= phone_number

    def set_role(self, role):
        self.role= role  
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.full_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_role(self):
        return self.role  