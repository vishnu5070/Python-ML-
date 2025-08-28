import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x=np.array([20,22,25,27,30,32,35,38]).reshape(-1,1)
y=np.array([50,60,70,75,85,90,100,110])
model=LinearRegression()
model.fit(x,y)
intercept=model.intercept_
slope=model.coef_[0]
print(f"intercept(c):{intercept}")
print(f"slope(m):{slope}\n")
new_temperature=np.array([[33]])
predicted_sales=model.predict(new_temperature)
print(f"predicted sales for 33 c :{predicted_sales[0]} cups")
y_pred_all=model.predict(x)
plt.scatter(x, y, color='blue', label='Original Data')
#plt.scatter(x,y,colour='blue', label='Original Data')
plt.plot(x, y_pred_all, color='red', linewidth=2, label='Linear Regression Line')
plt.title('lemonade Sales vs temperature')
plt.xlabel('tempature(c)')
plt.ylabel('cups sold')
plt.legend()
plt.grid(True)
plt.show()
