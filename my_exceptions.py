#! /usr/bin/env python3

class MyException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class MyException_1(MyException):
    def __init__(self):
        super().__init__(self,("Test exception #1"))

class MyException_2(MyException):
    def __init__(self):
        super().__init__(self,("Test exception #2"))
