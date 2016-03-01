from pprint import pprint

"""Problem statement: Loop through data and convert to a dictionary with
dictionaries. The end product should look like this :
{
    'first': {
        '0': ('600', '900', '50', '100', '0.02'),
        '1': ('600', '900', '50', '100', '0.02')
    },
    'second' : {
        '4': ('600', '900', '50', '100', '0.02')
    }
}
"""

data = [('first', '0', '600', '900', '50', '100', '0.02'),
        ('first', '1', '600', '900', '50', '100', '0.02'),
        ('first', '2', '600', '900', '50', '100', '0.02'),
        ('first', '3', '600', '900', '50', '100', '0.02'),
        ('second', '4', '600', '900', '50', '100', '0.02'),
        ('second', '5', '600', '900', '50', '100', '0.02'),
        ('second', '6', '600', '900', '50', '100', '0.02'),
        ('second', '7', '600', '900', '50', '100', '0.02'),
        ('third', '8', '600', '900', '500', '1000', '0.01'),
        ('third', '9', '600', '900', '500', '1000', '0.01'),
        ('third', '10', '600', '900', '500', '1000', '0.01'),
        ('first', '11', '600', '900', '50', '100', '0.02')]


sorted_dict = {}

for row in data:
    if row[0] not in sorted_dict:
        sorted_dict[row[0]] = {}
    sorted_dict[row[0]][row[1]] = row[2:]

pprint(sorted_dict)


# Another method
"""
from collections import defaultdict
# whenever a key doesn't exist yet, it will be created,
# with the value being a new empty dictionary
sorted_dict = defaultdict(lambda: {})

# this works whether or not data[key] has ever been assigned to
for row in data:
    sorted_dict[row[0]][row[1]] = row[2:]

pprint(sorted_dict)
"""
