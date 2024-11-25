import pandas as pd
import matplotlib.pyplot as plt
arch = pd.read_csv("dec1.csv")
print(arch.head(10))
fig = plt.figure()
fig.clf()
ax = fig.subplots(2,2)
 
ax[0,0].plot(range(len(arch["40 - 50"])),arch["40 - 50"],"o",color = "red")
ax[0,0].set_xlabel('Referencia')
ax[0,0].set_ylabel('40 - 50 %')
ax[0,0].set_title('Grafica 1')
 
ax[0,1].plot(range(len(arch["40 - 50"])),arch["30 - 40"],"o",color = "blue")
ax[0,1].set_xlabel('Referencia')
ax[0,1].set_ylabel('30 - 40 %')
ax[0,1].set_title('Grafica 2')
 
ax[1,0].plot(range(len(arch["40 - 50"])),arch["20 - 30"],"o",color = "yellow")
ax[1,0].set_xlabel('Referencia')
ax[1,0].set_ylabel('20 - 30 %')
ax[1,0].set_title('Grafica 3')
 
ax[1,1].plot(range(len(arch["40 - 50"])),arch["0 - 10"],"o",color = "green")
ax[1,1].set_xlabel('Referencia')
ax[1,1].set_ylabel('0 - 10 %')
ax[1,1].set_title('Grafica 4')
 
fig.tight_layout()
fig.show()     