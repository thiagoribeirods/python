def fatorial(n):
  if n == 1:
    return 1
  return n * fatorial(n-1)

def potencia(n,e):
  if e == 1:
    return n
  else:
    return n * potencia(n, e-1)

def multiplica(n,e):
  if e == 1:
    return n
  return n + multiplica(n, e-1)

a = fatorial(2)

b = potencia(2, 3)

c = multiplica(2, 3)
print('fatorial ->', a)
print('potencia -> ', b)
print("multiplica -> ", c)
