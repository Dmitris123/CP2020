from math import log

def f(x):
    if x == 0:
        # предел $x^2 log(x)$ при $x-> 0$ равен нулю, хотя log(x) не определен в x=0
        return 0.0
    else:
        return x**2 * log(x)
    
def fder(x):
    if x == 0:
        return 0.0
    else:
        return x*(2*log(x) + 1)

x = 0
def deriv(f,x,h):
    numerator=-1.5*f(x)+2*f(x+h)-0.5*f(x+2*h)
    denumerator=h
    return numerator/denumerator

for h in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10,1e-20,1e-20,1e-40,1e-80,1e-160,1e-320]:
    err = deriv(f, x, h) - fder(x)
    print("%5f -- %7.4g" % (h, err))
    
# продлив интервал значений h так, чтобы посчитанный минимум ошибки в прошлом пункте в него попадал, мы получили следующее:
# при подставлении ненулевых значений можно было заметить очевидный минимум ошибки около h = 1e-6
# при x = 0 ошибка убывает до "падения" в машинный ноль
# так как итоговая ошибка складывается из двух ошибок: округления и линеаризации
# error = [приблизительно равно] = epsilon*(f(x)/h) + c*f3(x)*h^3
# первый член зануляется, так как наша фугкция в нуле равна нулю
# второй член зануляется, так как посчитанный предел при h стремящимся к нулю есть ноль