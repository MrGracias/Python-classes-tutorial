'''
Created on Dec 29, 2019

@author: ogracias
'''
class Employee:
    def __init__(self, first, last, pay):
        self.fn = first
        self.ln = last
        self.py = pay
        self.email = first + '.' + last + '@icloud.com'

    def fullName(self):
        return "{} {}".format(self.fn, self.ln)
        
emp_1 = Employee('Oscar', 'Gracias', 50000)
emp_2 = Employee('Test', 'User', 60000)


print(emp_1.fullName())






