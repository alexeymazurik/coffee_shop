def  isNumber(num):
        try:
            float(num)
            return True
        except Exception:
            return False

    
def checkInput(string):
        a = ''
        while (not isNumber(a)):
            a = raw_input(string)
        return a