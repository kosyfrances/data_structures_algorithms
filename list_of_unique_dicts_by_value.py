""" copied from http://stackoverflow.com/questions/11092511/python-list-of-unique-dictionaries

Lets say I got a list of dictionaries:
[
{'id':1,'name':'john', 'age':34},
{'id':1,'name':'john', 'age':34},
{'id':2,'name':'hanna', 'age':30},
]
and I need to obtain a list of unique dictionaries (removing the duplicates):
[
{'id':1,'name':'john', 'age':34},
{'id':2,'name':'hanna', 'age':30},
]
What is the most efficient way to achieve this?
"""
list_of_dict = [
    {'id': 1, 'name': 'john', 'age': 34},
    {'id': 1, 'name': 'john', 'age': 34},
    {'id': 2, 'name': 'hanna', 'age': 30},
]

sorted_list = {v['id']: v for v in list_of_dict}.values()
print "sorted list is " sorted_list

"""
If you have two lists and you want to merge those lists and sort with different keys
"""

L1 = [
    {'id': 1, 'name': 'john', 'age': 34},
    {'id': 1, 'name': 'john', 'age': 34},
    {'id': 2, 'name': 'hanna', 'age': 30},
    {'id': 1, 'name': 'john', 'age': 34},
]

L2 = [
{'sn': 2, 'name': 'hanna', 'age': 30} ,
{'sn': 3, 'name': 'han', 'age': 30},
{'sn': 2, 'name': 'hanna', 'age': 30},
]
L3 = L1 + L2

sorted_merged_list = {v.get('id') or v.get('sn'): v for v in L3}.values()
print "Sorted merge list is, " sorted_merged_list
