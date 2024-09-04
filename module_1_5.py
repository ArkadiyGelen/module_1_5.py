immutable_var = 1, 2, "a", "b"
print(immutable_var)
#immutable_var [0] = 3    не изменяемый кортедж
mutable_list = [1, 2, "a", "b"]
print(mutable_list)
mutable_list .append("Modified")
print(mutable_list)