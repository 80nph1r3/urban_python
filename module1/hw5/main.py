from collections.abc import MutableSet


immutable_var = (1, "a", [])
print(immutable_var)

# Ошибка, кортеж - неизменяемый тип данных
immutable_var[0] = 2

# Однако если элемент кортежа является изменяемым типом, то его можно изменить
immutable_var[2].append("hey")
print(immutable_var)

mutable_list = [2, "b", tuple()]
mutable_list[1] = "c"
print(mutable_list)
