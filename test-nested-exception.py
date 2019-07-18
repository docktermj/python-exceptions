#! /usr/bin/env python3

from my_exceptions import MyException_1, MyException_2

def function_1():
    raise MyException_1
    print("We shouldn't get here.")
    return 5

def function_2():
    try:
        function_1()
    except Exception as err:
        print("Function 2 err type {0}".format(type(err)))
        raise err

try:
    return_code = function_2()
except MyException_1 as err:
    print("MyException_1: {0}".format(err))
except MyException_2 as err:
    print("MyException_2: {0}".format(err))
except Exception as err:
    print("Exception: {0}".format(err))
except:
    print("Simple except")

print("Return code: {0}".format(return_code))
