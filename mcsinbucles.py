#En este nuevo ejericio se busca eliminar
#completamente el uso de bucles for
import numpy as np
import matplotlib.pyplot as plt
from time import time
#Obtenemos un vector que nos de el dato de N
#equiespaciado

N = np.logspace(2,8,num=10,endpoint=True)
N = np.around(N).astype(int)

#Se busca crear la matriz de datos x,y aleatorios
#juntamente con su distancia para el grupo más grande
#y seleccionar para el cálculo de subgrupos como un subconjunto del grande

tiempo_inicial = time() 
a=N[N.size-1]
rand=np.random.random((a,2))

#En última instancia nos interesa unicamente el vector distancias y si cumple 
#el criterio de ser mayor al radio (tipo boolean) 
z=np.sqrt(rand[:,0]**2+rand[:,1]**2)<=1
#Usaremos el indexado lógico que permite python

#generaremos una lista que contenga cada vector con N indices random
#Aqui recurriremos a una indexación del vector lógico de distancias 
#con un array de indices

error=[np.absolute((4/i)*z[np.arange(0,i)].sum()-np.pi) for i in N] #los bucles dentro de indices
                                                                    #son optimizados en python.

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecución del programa fue ',tiempo_ejecucion,' segundos')

#generamos la gráfica
plt.figure()

plt.plot(np.arange(1,11),error,'o-')
plt.xticks(range(1,N.size+1), N, rotation=20)
plt.xlabel('Número de pruebas')
plt.ylabel('Error abs Pi por MC')
plt.grid(True)
plt.show()