immutable_var = 1,2,3,4
immutable_var_2 = (1,2,3,4)
immutable_var_3 = (1,2,3,4)
print(immutable_var)
print(immutable_var_2)
print(immutable_var_3) #кортежи- это незименяемые тип данных
mutable_list = ['apple', 'mango', 'pear']
print(mutable_list)
print(mutable_list[0])
mutable_list [1] = 'meal'
print(mutable_list)
print(mutable_list[1])
mutable_list.append(False)
print(mutable_list)
mutable_list.extend(['Modified', 2])
print(mutable_list)
mutable_list.remove('pear')
print(mutable_list)
print('apple' in mutable_list)
print('apple'not in mutable_list)

