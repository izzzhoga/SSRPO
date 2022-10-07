import copy

users = ['Alex', 'Bob', 'Ilya', 'Alice']
print(users)

users.append('Jhon')
print(users)

users.insert(2, 'Greg')
print(users)

users.insert(0, ['1, 2, 3, 4'])
print(users)

index_list = users.index(['1, 2, 3, 4'])
print(index_list)

users.insert(5, [4, 3, 2, 1])
print(users)

index_list = users.index([4, 3, 2, 1])
print(index_list)

users_2 = users
users_3 = copy.deepcopy(users)
users_2.append('copy')
users_3.append('copy_2')
print(users)
print(users_2)
print(users_3)

print()
print(users_3[1:6:2])

users_list = [[1, 'one'],[2, 'two'],[3, 'three']]
users_dict = dict(users_list)
print(users_dict)