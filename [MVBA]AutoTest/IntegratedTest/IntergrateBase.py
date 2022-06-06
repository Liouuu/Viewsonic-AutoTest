import unittest
from Library.LibWebDriver import LibWebDriver
from Library.LibLogHelper import LogPackage


class IntergrateBase(unittest.TestCase):

    def __init__(self, driver: LibWebDriver, log: LogPackage):
        self.Driver: LibWebDriver = driver
        self.Log: LogPackage = log
