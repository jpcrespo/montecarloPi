''' En el siguiente método se busca reducir el uso
bucles para resolver el problema. En el anterior 
ejercicio se usaron dos bucles for para la solucion.
En esta propuesta reduciremos el uso a un solo bucle 
FOR '''

import numpy as np
import matplotlib.pyplot as plt
from time import time



N = np.logspace(2,8,num=10,endpoint=True)
N = np.around(N).astype(int)
A=[]
pis=[]

tiempo_inicial = time() 



for i in N:
    a = np.random.random((i,2))
    z=np.sqrt(a[:,0]**2+a[:,1]**2)
    a_sc1=z<=1
    a_sc=np.sum(a_sc1)
    pi = 4*a_sc/i
    pis.append(pi)
    A.append(np.absolute(pi-np.pi))
    
print(pis)    
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('El tiempo de ejecución del programa fue ',tiempo_ejecucion,' segundos')

#generamos la gráfica
plt.figure()
plt.plot(np.arange(1,11),A,'o-')
plt.xticks(range(1,N.size+1), N, rotation=20)
plt.xlabel('Número de pruebas')
plt.ylabel('Error abs Pi por MC')
plt.grid(True)
plt.show()