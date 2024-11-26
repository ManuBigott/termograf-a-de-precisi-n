import pandas as pd
import matplotlib.pyplot as plt
arch = pd.read_csv("dec1.csv")
print(arch.head(10))
fig = plt.figure()
fig.clf()
ax = fig.subplots(2,2)
 
ax[0,0].plot(range(len(arch["40 - 50"])),arch["40 - 50"],"o",color = "red")
ax[0,0].set_xlabel('Tiempo')
ax[0,0].set_ylabel('% entre 40 - 50 grados')
ax[0,0].set_title('40 - 50')
 
ax[0,1].plot(range(len(arch["40 - 50"])),arch["30 - 40"],"o",color = "blue")
ax[0,1].set_xlabel('Tiempo')
ax[0,1].set_ylabel('% entre 30 - 40 grados')
ax[0,1].set_title('30 - 40')
 
ax[1,0].plot(range(len(arch["40 - 50"])),arch["20 - 30"],"o",color = "yellow")
ax[1,0].set_xlabel('Tiempo')
ax[1,0].set_ylabel('% entre 20 - 30 grados')
ax[1,0].set_title('20 - 30')
 
ax[1,1].plot(range(len(arch["40 - 50"])),arch["0 - 10"],"o",color = "green")
ax[1,1].set_xlabel("Tiempo")
ax[1,1].set_ylabel('% entre 0 - 10 grados')
ax[1,1].set_title('0 - 10')
 
fig.tight_layout()
fig.show()     