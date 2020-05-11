from math import sin
from scipy.special import sici

x1 = 0
x2 = 1

e = 1e-4

def func(x):
    return sin(x**0.5)/x

true_int = 2*sici(1)[0]

def cent_int(f,a,b,eps):
    h = eps**0.5
    summ = 0
    xi = a + h/2
    while(xi < b):
        summ = summ + h*f(xi)
        xi = xi + h
    return summ
    
def err(a,b):
    return abs(a-b)

print (err(true_int,cent_int(func,x1,x2,e)))
# при подсчёте в лоб получается погрешность на ДВА ПОРЯДКА БОЛЬШЕ, чем заданная ошибка e
# (при условии если считать погрешность подсчёта функции si из библиотеки scipy.special очень малой) 

def func1(x):
    return sin(x**0.5)/x - 1/x**0.5

print (err(true_int,cent_int(func1,x1,x2,e)+2))
# (двойка возникает из-за взятия интеграла от 1/x**0.5 аналитически)
# в последнем выражении уже видно, что погрешность ВХОДИТ в интервал заданной ошибки

## далее я не совсем понял формулировку "Сравните количество необходимых итераций для достижения заданной точности e"
## так что посчитаю, сколькро нужно сделать итераций, чтобы получить такую же точность в лоб
#
#def cent_int1(f,a,b,n):
#    h = abs(a-b)/n
#    summ = 0
#    xi = a + h/2
#    while(xi < b):
#        summ = summ + h*f(xi)
#        xi = xi + h
#    return summ
#
#n = 100
#while (n < 1e100):
#    if err(true_int,cent_int1(func,x1,x2,e)) > e:
#        n = n * 10
#    else:
#        break
#
#print (n)
