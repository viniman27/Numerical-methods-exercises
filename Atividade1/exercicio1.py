import math as m

# Variaveis

a = 14.75
b = - 5.92 
c = 61.4
d =  0.6*((a*b) - c)

euler = m.e

# Equacoes

eqA = ((a*b)/c)*((a+d**2)/m.sqrt(abs(a*b)))

eqB = d*(euler**(d/2)) + (((a*d)+(c*d))/((25/a)+(35/b))/(a+b+c+d))


print('letra a: ', eqA)
print('letra b: ', eqB)