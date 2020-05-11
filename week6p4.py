x1 = 0
x2 = 2

e = 1e-10

def func(x):
    return x**3

true_integral = 4

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

print (err(true_integral,cent_int(func,x1,x2,e)))
print (err(true_integral,cent_int(func,x1,x2,e/4)))
    
#полученные результаты попадают в интервал заданной ошибки
