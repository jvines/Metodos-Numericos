'''
Tarea 02 FI3104
Jose Vines.
'''

'''
En este codigo se encuentran los puntos en donde dos funciones, F1 y F2, definidas mas abajo, se hacen 0 simultaneamente.
'''

import scipy as sp
import scipy.optimize as opt
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def F1(x, y):
	'''
	Funcion 1 del enunciado
	'''
    res = x**4 + y**4 - 15
    return res

def F2(x, y):
	'''
	Funcion 2 del enunciado
	'''
    RRR = 1.464
    res = x**3*y - x*y**3 - y/2. - RRR
    return res

'''
Primero se van a graficar las funciones y sus contornos en el nivel 0, es decir en donde se hacen 0
'''

x = sp.linspace(-3, 3, 300)
y = sp.linspace(-2, 2, 200)
levels = [0]
X, Y = sp.meshgrid(x, y)
Z1 = F1(X, Y)
Z2 = F2(X, Y)

plt.imshow(Z1, origin='lower', cmap=cm.viridis, extent=(-3, 3, -2, 2))
plt.contour(X, Y, Z1, levels)

plt.savefig('contour_f1.png')

plt.clf()

plt.imshow(Z2, origin='lower', cmap=cm.viridis, extent=(-3, 3, -2, 2))
plt.contour(X, Y, Z2, levels)

plt.savefig('contour_f2.png')

plt.clf()

'''
Luego se grafican ambos contornos en nivel 0 para analizar mejor las intersecciones.
'''

plt.contour(X, Y, Z1, levels)
plt.contour(X, Y, Z2, levels)

plt.savefig('intersecciones.png')

'''
Usando el hint de la parametrizacion, se infiere que la parametrizacion de y es la misma cambiando el seno por coseno
y la constante de proporcionalidad debe ser la raiz cuarta de 15.
Usando esta informacion se encuentra que los ceros de F2 estan separados por una distancia de pi/4 aproximadamente.
Luego se reduce la funcion F2 a una sola variable, t, a traves de la parametrizacion
'''

def F2_reducida(t):
	'''
	Funcion 2 del enunciado reducida a una sola variable.
	'''
	C = 1.9679896712654303
    x = sp.sign(sp.sin(t)) * sp.power(sp.sin(t)**2, 1./4.)*C
    y = sp.sign(sp.cos(t)) * sp.power(sp.cos(t)**2, 1./4.)*C
    res = F2(x, y)
    return res

'''
Haciendo uso del scipy.optimize.bisect se encuentran los ceros de la funcion 2 a traves de la siguiente funcion
'''

def encuentra_ceros(tol = 1e-20):
	'''
	Funcion que encuentra los puntos en donde la funcion 2 se hace 0.

	Parameters
    ----------
    tol : int or float
        Tolerancia con la que se busca la raiz.
    
    Returns
    -------
    res : list(float)
        Una lista con los pares x,y en donde la funcion 2 se hace 0.
	'''
	C = 1.9679896712654303
    pi = sp.pi
    posibles_ceros = [pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4, 2*pi]
    delta = [.5, -.5]
    pares = []
    for t in posibles_ceros:
        if F2_reducida(t)*F2_reducida(t+delta[0])<0:
            t_0 = opt.bisect(F2_reducida, t, t+delta[0], xtol=tol)
        else:
            t_0 = opt.bisect(F2_reducida, t, t+delta[1], xtol=tol)
        x = sp.sign(sp.sin(t_0)) * sp.power(sp.sin(t_0)**2, 1./4.)*C
        y = sp.sign(sp.cos(t_0)) * sp.power(sp.cos(t_0)**2, 1./4.)*C
        pares.append((x, y))
    return pares
