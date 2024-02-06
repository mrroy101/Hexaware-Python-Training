class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.setRole(role)

    @property
    def getUserId(self):
        return self.userId

    @property
    def getUsername(self):
        return self.username

    @property
    def getPassword(self):
        return self.password

    @property
    def getRole(self):
        return self.role


    def setUserId(self, userId):
        self.userId = userId

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setRole(self, role):
        if role not in ['Admin' , 'User']:
            raise Exception("The role should be Admin or User")
        self.role = role

u1 = User(101,'sankar','root','Admin')
u1.setRole('User')
print(u1.getRole)
