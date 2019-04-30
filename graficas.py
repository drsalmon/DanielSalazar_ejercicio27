import numpy as np
import matplotlib.pyplot as plt

a = os.system("g++ DanielSalazar_ej27.cpp -o DanielSalazar_ej27.x")
a = os.system("./DanielSalazar_ej27.x > DanielSalazar_ej27.dat")

plt.figure()
data = np.loadtxt("DanielSalazar_ej27.dat")
plt.plot(x,y, label='resultado esperado')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig("ejercicio.png")