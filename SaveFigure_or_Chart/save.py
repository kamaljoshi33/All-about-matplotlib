import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [30,10,40,20,50]

fig, ax = plt.subplots(1,2, figsize=[10,5])
ax[0].plot(x,y, color='blue')
ax[0].set_title('Line data')


ax[1].bar(x,y, color='purple')
ax[1].set_title('bar data')


plt.tight_layout()  # it automatically set the height width of the plot
fig.suptitle('comparesion of line and bar chart')


plt.show()
plt.savefig('plot.pdf', dpi=300, bbox_inches='tight')




