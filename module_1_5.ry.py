immutable_var = ('Timon','Pumba','Friendship',123,46,5)
print('Immutable tuple: ',immutable_var)
# четвёртая комада будет давать ошибку
#immutable_var[1] = 54
# Изменение картежа невозможно, так как это неизменяемый элемент. Возможно изменение только списка входящего в кортеж, если таковой имеется.
mutable_list = ('Timon','Pumba','Friendship', [54,33,126])
#print(mutable_list)
mutable_list[3][2] = 34
#print(mutable_list)
print('Mutable list: ',mutable_list[3])