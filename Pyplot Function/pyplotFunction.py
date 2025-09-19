import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
y = [5,4,2,6,1]
plt.plot(x,y)
plt.title('Backery sales is of this week')
plt.xlabel('days of week')
plt.ylabel('no of cake show')
plt.show()



# pyplot function -
# plt.plot(x,y,color='red', line="style", linewidth=value, marker='marker symbol', label = 'label-name')


month = [1,2,3,4,5]
data = [10,12,16,58,3]
plt.plot(month,data, color='red', linestyle='--', linewidth=2, marker = 'o', label='2025 sales data')
plt.xlabel('months')
plt.ylabel('data')
plt.title('Monthly data report')
plt.legend(loc='lower right') # upper left or lower right used or they are optional 
plt.grid(color='orange', linestyle='dotted') 
plt.xticks( [1,2,3,4], ['M1', 'M2', 'M3', 'M4'])    # we can use it for x and y line also
plt.yticks(color='brown')
plt.ylim(0,100)
plt.xlim(1,5)
plt.show()



