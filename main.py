from functools import reduce

lista = [1,2,3,4,5,6,7,8,9]

def impar(x):
    if(x%2 != 0):
        return True

#impares = filter(impar, lista)
impares = filter(lambda x: x%2 != 0 , lista)
impares = list(impares)
print(impares)

suma = reduce(lambda x,y: x+y, impares)
print(suma)