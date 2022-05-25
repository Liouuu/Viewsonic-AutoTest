class LibData:
    @staticmethod
    def StringMerge(merge, *params):
        result = ""
        for param in params:
            if(result and LibData.__LastExist(merge, result)):
                result = result+merge
            result = result+str(param)
        return result

    @staticmethod
    def __LastExist(merge, strVal):
        mergeLen = len(merge)
        strLen = len(strVal)
        if(strLen-mergeLen < 1):
            return True
        return not strVal[-mergeLen:] is merge
