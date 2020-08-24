import cProfile
import re


i = 0
k=1
j=2

def and_condition():
    if i == 0 and k == 1 and j == 2:
        print("in here")

def all_condition():
    if all((i == 0,k == 1,j == 2)):
        print("in here")

def or_condition():
    if i == 0 or k == 1 or j == 2:
        print("in here")

def any_condition():
    if any((i == 0,k == 1,j == 2)):
        print("in here")

cProfile.run('re.compile("and_condition")')
cProfile.run('re.compile("all_condition")')
cProfile.run('re.compile("or_condition")')
cProfile.run('re.compile("any_condition")')