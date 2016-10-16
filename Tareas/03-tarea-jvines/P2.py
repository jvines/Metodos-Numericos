'''
P2 Tarea 03 FI3104
Jose Vines.
'''

'''
En este codigo se carga una imagen con pixeles muertos como una matriz de
floats, a la cual se interpola un Spline de dos variables para reconstruir
dichos pixeles.
'''

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import scipy as sp
import scipy.interpolate as inter
from skimage import io, img_as_float

'''
Se carga la imagen y se convierte en una matriz de floats.
Se muestra la imagen y una estampilla de esta al rededor de los pixeles
danados.
'''
img = io.imread('galaxia.bmp')
img = img_as_float(img)

mask = io.imread('mask.bmp')
mask = img_as_float(mask)

plt.figure(1)
plt.clf()
plt.imshow(img, interpolation='nearest')

stamp = img[140:165, 117:167]

plt.figure(2)
plt.clf()
plt.imshow(stamp, cmap=cm.gray, interpolation='nearest')
plt.show()

'''
stamp_xy : matriz con las posiciones x e y del borde de la estampilla
good_pixels : matriz con los indices de los pixeles buenos
damaged_pixels_stamp : matriz con los indices donde los pixeles estan muertos
                       en la estampilla
damaged_pixels : matriz con los indices donde los pixeles estan muertos en la
                 imagen original
'''
stamp_xy = sp.array([sp.arange(0, 25), sp.arange(0, 50)])
good_pixels = sp.where(stamp[:, :, 0] != 0)
damaged_pixels_stamp = sp.where(stamp[:,:,0]==0)
damaged_pixels = sp.where(mask==1)

'''
Se hace la interpolacion con Spline para cada capa de la imagen y luego se
unen para visualizar el Spline "total".
'''

splR = inter.SmoothBivariateSpline(good_pixels[0], good_pixels[1],
                                   stamp[good_pixels[0], good_pixels[1],0])
splG = inter.SmoothBivariateSpline(good_pixels[0], good_pixels[1],
                                   stamp[good_pixels[0], good_pixels[1],1])
splB = inter.SmoothBivariateSpline(good_pixels[0], good_pixels[1],
                                   stamp[good_pixels[0], good_pixels[1],2])

new_img = sp.dstack([splR(stamp_xy[0],stamp_xy[1]),
                     splG(stamp_xy[0],stamp_xy[1]),
                     splB(stamp_xy[0],stamp_xy[1])])

plt.imshow(new_img)

'''
Se arregla la imagen cambiando los pixeles muertos por los nuevos pixeles aproximados.
'''
fxdR = img[:,:,0]
fxdG = img[:,:,1]
fxdB = img[:,:,2]

fxdR[damaged_pixels[0],damaged_pixels[1]] = new_img[damaged_pixels_stamp[0], damaged_pixels_stamp[1], 0]
fxdG[damaged_pixels[0],damaged_pixels[1]] = new_img[damaged_pixels_stamp[0], damaged_pixels_stamp[1], 1]
fxdB[damaged_pixels[0],damaged_pixels[1]] = new_img[damaged_pixels_stamp[0], damaged_pixels_stamp[1], 2]

fxd_img = sp.dstack([fxdR,fxdG,fxdB])

plt.imshow(fxd_img)
plt.savefig('fixed_galaxy.pdf')