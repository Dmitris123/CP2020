import numpy as np
import matplotlib.pyplot as plt
import pylab

A = np.array([[-10, 10], [32, -499]])
val = np.sort(abs(np.linalg.eigvals(A))) #собственные значения
print (abs(max(val)/abs(min(val))))
# полученное значение на порядок больше единицы, поэтому система должна быть жёсткой

# а как решать матричные уравнения не понял