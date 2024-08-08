my_dict = {'Mazda':124, 'Opel': 545, 'Tayota': 643, 'Mercedec':245}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Opel'))
my_dict.update({'BMW': 154, 'Audi': 423})
a = my_dict.pop('Mazda')
print(my_dict.get('Mazda'), 'Not existing value: None')
print('Deleted value: ', a)
print('Modified dictionary: ',my_dict)

my_set = {'Masha', 123,3,3,4,'Masha', 'Conja'}
print('Set: ', my_set)
#my_set.add(78)
#my_set.add('Nona')    или 14 в одно действие
my_set.update([78,'Nona'])
my_set.remove(123)
print('Modified set: ',my_set)


