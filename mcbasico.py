import numpy as np
import matplotlib.pyplot as plt
from time import time


A=[]
pi=[]

N = np.logspace(2,8,num=10,endpoint=True)
N = np.around(N).astype(int) #numeros enteros

tiempo_inicial = time() 

#Calculamos los numeros random

for i in N:
    count = 0
    for j in range(i):
        x = np.random.random()
        y = np.random.random()
        dist = np.sqrt(x**2+y**2)
        if dist < 1:
            count = count +1 
    piexp=4*count/i   
    pi.append(piexp)
    A.append(np.absolute(piexp-np.pi))
    

print(pi)
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