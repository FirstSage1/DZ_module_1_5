# Неизменяемые и изменяемые объекты. Кортежи.
 #  + Списки.Индексации и методы списков
  # ==================================================
#  Кортеж.Неизменяемый объект.
immutable_var=(3,49,0,1,True, "привет", "!")
print(immutable_var)
print(type(immutable_var))
#immutable_var[0]= 7
#print(immutable_var)
# ----------------------------------------------------------------
#  Списки.Изменяемый объект.
mutable_list=[ 3,49,0,1,True, "привет", "!"]
print(mutable_list)
print(type(mutable_list))
print(mutable_list[0])
mutable_list[0]= 7
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
