import matplotlib.pyplot as plt

area = ['Sun','mon','tue','wed']
data = [200,300,100,500]
plt.pie( data, labels=area, autopct='%1.1f%%', colors=['gold','red','purple','brown'])
plt.title('total sales')
plt.show()