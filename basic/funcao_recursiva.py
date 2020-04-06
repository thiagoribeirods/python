#Recursivo
def fatorialR(n):
  if n == 0:
    return 1
  return n*fatorialR(n-1)

print(fatorialR(0))

#Iterativo
print("^"*20)

def fatorialI(n):
  fat = n
  for i in range(n,1, -1):
    fat = fat * (i-1)
  return fat
print(fatorialI(10))
