immutable_var = 'я родился в', 19, [8, 1], 'году', True
# immutable_var[2]= 18 # кортеж не поддерживает обращение по элементам
print(immutable_var)
print()

mutable_list = [1, 9, 8, 1]
print(mutable_list)
mutable_list[2] = 1
mutable_list[3] = 8
print(mutable_list)
