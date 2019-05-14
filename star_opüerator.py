def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(0, 1, 0)

tupl_vec = (1, 0, 1)
list_vec = [1, 0, 1]
print_vector(tupl_vec[0],
             tupl_vec[1],
             tupl_vec[2])


print_vector(*tupl_vec)
print_vector(*list_vec)

genexpr = (x * x for x in range(3))
print_vector(*genexpr)


dict_vec = {'y': 0, 'x': 1, 'z': 1}
print_vector(**dict_vec)

print_vector(*dict_vec)
