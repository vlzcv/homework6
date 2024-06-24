my_dict = {'Vlada' : 2009, 'Vova' : 2004}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vlada'])
print('Not existing value:', my_dict.get('Dima'))
my_dict.update({"Nastya" : 2006, "Vasya" : 2004})
print('Deleted value:', my_dict['Vasya'])
del my_dict['Vasya']
print(my_dict)

my_set = {1,2,3,2,1,3,'String',(1,2,3)}
print('Set:', my_set)
my_set.add(5)
my_set.add('hello')
my_set.discard(('String'))
print('Modified set:', my_set)



