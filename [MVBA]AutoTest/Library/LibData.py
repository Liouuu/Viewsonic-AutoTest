from inspect import getmembers, isfunction
import inspect


class LibData:
    @staticmethod
    def Merge(merge, *params):
        result = ""
        for param in params:
            if(result and LibData.__LastExist(merge, result)):
                result = result+merge
            result = result+str(param)
        return result

    @staticmethod
    def AddExtention(fileName: str, extention: str):
        return fileName+extention if LibData.__LastExist(extention, fileName) else fileName

    @staticmethod
    def __LastExist(merge, strVal):
        mergeLen = len(merge)
        strLen = len(strVal)
        if(strLen-mergeLen < 1):
            return True
        return not strVal[-mergeLen:] is merge

    @staticmethod
    def In(val, *elements):
        for element in elements:
            if(type(val) == type(element) and val == element):
                return True
        return False

    @staticmethod
    def DynamicExecClassFunction(methodClass, *args):
        for item in getmembers(methodClass, isfunction):
            item[1](*args)
