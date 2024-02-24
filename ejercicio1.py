# Matriz inicial
ejemplo1 = [[9,  8,  7],

            [6,  5,  4],

            [3,  2,  1]]



print("La matriz original  desordenada:")
for row in ejemplo1:
    print(row)

# Ordenar la matriz
for row in ejemplo1:
    row.sort()

# Mostrar matriz ordenada
print("\n La matriz esta  ordenada:")
for row in ejemplo1:
    print(row)
