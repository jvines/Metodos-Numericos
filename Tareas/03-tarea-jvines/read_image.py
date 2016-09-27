#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este script lee dos imagenes bmp con scikit-image y transforma los valores de
los pixeles en floats en el rango [0-1].

img tiene 3 capas correpondientes a los colores rojo, verde y azul.
mask tiene una sola capa, es una mascara que indica los pixeles malos (con
valor 1) y los pixeles buenos (con valor 0).

El script crea 2 figuras que muestran img y luego un pedazo de img, en las
cercanías de la región con pixeles malos.

Para resolver la tarea necesitará fitear una spline2D a la imagen. Si intenta
fitear la spline a toda la imagen, puede que su computador demore demasiado. Es
recomendable solo fitear el area cercana a los pixeles malos.

Su objetivo es usar los pixeles buenos para crear la spline2D y luego
reemplazar los pixeles malos por los valores interpolados a traves de la
spline2D que creo.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage import io, img_as_float

img = io.imread('galaxia.bmp')
img = img_as_float(img)

mask = io.imread('mask.bmp')
mask = img_as_float(mask)

plt.figure(1)
plt.clf()
plt.imshow(img, interpolation='nearest')

plt.figure(2)
plt.clf()
plt.imshow(img[140:170, 110:170], cmap=cm.gray, interpolation='nearest')
plt.show()


## En esta seccion, Ud debe arreglar la imagen ===

## ===============================================
# Para guardar la imagen al final del proceso
# io.imsave('galaxia-arreglada.png', img)






