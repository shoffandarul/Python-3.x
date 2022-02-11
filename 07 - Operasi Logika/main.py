# NOT -> kebalikan nilai
a = True
b = not a
print('\n===== NOT =====')
print('nilai A =', a)
print('NOT A   =', b)

# OR -> bernilai true, jika salah satunya true (penjumlahan)
print('\n===== OR =====')
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)

a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

# AND -> bernilai true, jika semuanya true (perkalian)
print('\n===== AND =====')
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)

a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)

a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

# OR -> bernilai true, jika salah satunya true, tetapi bernilai false, jika semua nilainya true
print('\n===== XOR =====')
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)

a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)