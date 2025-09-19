import matplotlib.pyplot as plt

# here mathplotlib is our main package  
# .pyplot is a module used inside it to get readymate function
# plt is a standard text

x = [1,2,3,4,5]
y = [10,20,15,60,40]
plt.plot(x,y)
plt.show()
plt.savefig('plot1.pdf', dpi=300, bbox_inches='tight') # to save file in system
