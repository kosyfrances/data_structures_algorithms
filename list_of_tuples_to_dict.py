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
    if row[0] in sorted_dict:
        sorted_dict[row[0]].update({row[1]: row[2:]})
    else:
        sorted_dict[row[0]] = {}
        sorted_dict[row[0]].update({row[1]: row[2:]})

pprint(sorted_dict)
