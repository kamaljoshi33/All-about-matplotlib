# Scatter - it is used to find the co-relation between two variable
# ex- temp vs ice-cream sales

import matplotlib.pyplot  as plt

# data = [1,2,3,4,5,6,7,8,9]
# sales = [10,20,30,40,50,60,10,80,30]
# plt.scatter(data , sales , color='red', marker='o', label='student data')
# plt.legend(loc='lower right')
# plt.xlabel('week')
# plt.ylabel('sales')
# plt.title('total sales ')
# plt.grid(True)
# plt.show()



# for actual compresion
plt.scatter([1,2,3,4,5], [10,20,50,35,15], color='red' , label='class A')
plt.scatter([1,2,3,4,5], [20,50,30,80,9], color='purple', label='class b')
plt.title('compare both class marks')
plt.grid(True)
plt.show()
