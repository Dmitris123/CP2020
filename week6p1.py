def deriv(f,x0,h):
    num = -f(x0+2*h) + 4*f(x0+h) - 3*f(x0) #эта формула следует из разложения в Тейлора для f(x+h) и f(x+2h)
    den = 2*h
    return num / den
def func(x):
    return x**3
x0 = 0
h = 1e-5
y = deriv(func,x0,h)
print("Df = ",y)

x = 0
for h in [1e-2, 1e-3, 1e-4, 1e-5,1e-7,1e-10,1e-14,1e-19,1e-35,1e-70,1e-100,1e-200]:
    err = deriv(lambda x: x**3, x, h)
    print("%5f -- %7.4g" % (h, err))
# ответ совпадает с ожидаемым пристремлении h к нулю
# и ответ строго равен нулю при захождении в область машинного нуля