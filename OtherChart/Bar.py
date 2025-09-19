import matplotlib.pyplot as plt

month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY']
data = [20,50,30,80,120]
plt.bar(month, data, color='red')
# barh for horizontal data show 
plt.legend('Data of 2025')
plt.title('MONTHLY SALES')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()