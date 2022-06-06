from UnitBase import LoginAndActive


def Case1(self, email):
    LoginAndActive.Activate(self, "Test", email, email)


def Case2(self, email, password):
    LoginAndActive.NormalLogin(self, email, password)
