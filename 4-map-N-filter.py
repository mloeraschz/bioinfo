## TEMA 3: map(), filter() y list comprehension

## Función filter()

## Esta función permite establecer una función filtro y aplicarla a una lista
## Por ejemplo:

miLista = [1,2,3,4,5,6,7,8,9,10]

def miFiltro(x):
    return x % 2 == 0

print(filter(miFiltro,miLista))

# Esto también puede hacerse con List Comprehension

print([x for x in miLista if miFiltro(x)])

## Función map()

## Esta función permite aplicar la misma operación a cada elemento de una lista
## Por ejemplo:

miLista = ['Hola','Arizona','Nuevo León','AGUASCALIENTES']

def miOperacion(x):
    x = list(x)  
    for y in x:
        if 'a' == y:
            x[x.index(y)] = 'A'
        elif 'A' == y:
            x[x.index(y)] = 'a'
    x = ''.join(x)       
    return x

print(map(miOperacion,miLista))
