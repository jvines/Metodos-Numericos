'''
P1 Tarea 03 FI3104
Jose Vines.
'''

'''
En este codigo se lleva a cabo la interpolacion de una funcion gaussiana,
definida por f(x), con polinomios de Lagrange y Splines para un intervalo
[-1, 1] equiespaciado con 5 puntos, hasta llegar a 20 puntos
'''

import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.interpolate as inter


def f(x):
    '''
    Funcion gaussiana definida en el enunciado.
    '''
    res = sp.exp(-x**2/.05)
    return res

'''
Se grafica la funcion a fittear
'''
x = sp.linspace(-1, 1, 1000, endpoint=True)
f_modelo = f(x)
plt.clf()
plt.plot(x, f_modelo)
plt.title("$f(x) = e^{-x^{2}/0.05}$", fontsize=18)
plt.xlabel('$x$', fontsize=18)
plt.ylabel('$f(x)$', fontsize=18)
plt.grid()

points = [5, 10, 15, 20]

# Sampleo de interpolacion utilizando polinomiox de Lagrange
# con 5, 10, 15 y 20 puntos.
# Nota, la implementacion de Lagrange es numericamente inestable y no se
# recomienda samplear mas de 20 puntos (scipy.org)

model_label = "$f(x) = e^{-x^{2}/0.05}$"
lagrange_label = "Lagrange"
spline_label = "Spline"
diff_lag_label = model_label + " - " + lagrange_label
for pts in points:
    title = 'Interpolacion de polinomio en %d puntos\ncon polinomio de Lagrange.' % pts
    sample = sp.linspace(-1, 1, pts, endpoint=True)
    f_sampled = f(sample)
    pol = inter.lagrange(sample, f_sampled)
    plt.clf()
    plt.plot(x, f_modelo, label=model_label, color='b')
    plt.plot(x, pol(x), label=lagrange_label, color='g')
    plt.plot(x, f_modelo - pol(x), label=diff_lag_label, color='r')
    plt.title(title)
    plt.xlabel('$x$', fontsize=18)
    plt.ylabel('$f(x)$', fontsize=18)
    if pts == 5:
        plt.ylim(-1.1, 1.05)
    elif pts == 10:
        plt.ylim(-.5, 1.05)
    elif pts == 15:
        plt.ylim(-2.4, 2.4)
    else:
        plt.ylim(-1.3, 1.3)
    plt.grid()
    plt.legend(loc='lower center', shadow=True)
    plt.savefig('lagrange%01d.pdf' % pts)

# Sampleo de interpolacion utilizando un Spline con 5, 10, 15 y 20 puntos.
# Nota, la implementacion de Spline esta basada en FITPACK escrita en FORTRAN.
diff_spl_label = model_label + " - " + spline_label
for pts in points:
    title = 'Interpolacion de Spline en %d puntos\ncon Spline.' % pts
    sample = sp.linspace(-1, 1, pts, endpoint=True)
    f_sampled = f(sample)
    pol = inter.UnivariateSpline(sample, f_sampled, s=0)
    plt.clf()
    plt.plot(x, f_modelo, label=model_label, color='b')
    plt.plot(x, pol(x), label=spline_label, color='g')
    plt.plot(x, f_modelo - pol(x), label=diff_spl_label, color='r')
    plt.title(title)
    plt.xlabel('$x$', fontsize=18)
    plt.ylabel('$f(x)$', fontsize=18)
    if pts == 5:
        plt.ylim(-1., 1.05)
    else:
        plt.ylim(-.5, 1.05)
    plt.grid()
    plt.legend(loc='lower center', shadow=True)
    plt.savefig("spline%01d.pdf" % pts)

'''
Se grafica con escala logaritmica en y: la diferencia entre el polinomio de
Lagrange y la funcion, la diferencia entre el Spline y la funcion
'''

sample = sp.linspace(-1, 1, 50, endpoint=True)
f_sampled = f(sample)
pol1 = inter.UnivariateSpline(sample, f_sampled, s=0)
pol2 = inter.lagrange(sample, f_sampled)
plt.clf()
plt.semilogy(x, sp.fabs(pol1(x)-f_modelo), label=diff_spl_label, color='r')
plt.semilogy(x, sp.fabs(pol2(x)-f_modelo), label=diff_lag_label, color='g')
plt.title('Interpolacion de polinomio en 50 puntos con metodo de Spline y Lagrange.')
plt.xlabel('$x$', fontsize=18)
plt.ylabel('$f(x)$', fontsize=18)
plt.ylim(-1.1, 1.05)
plt.grid()
plt.legend(loc='lower center', shadow=True)
plt.savefig('lagrange_spl_diff.pdf')
