from UnitFunction import LoginAndActive
import sys
import os
sys.path.append(os.getcwd())


def Case1(self, email):
    LoginAndActive.Activate(self, "Test", email, email)


def Case2(self, email, password):
    LoginAndActive.NormalLogin(self, email, password)
