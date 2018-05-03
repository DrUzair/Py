# Line Plot
```python
import matplotlib.pyplot as plt
x1=[1, 2, 3, 4, 5]
y1=[1, 2, 3, 4, 5]
x2=[1, 2, 3, 4, 5]
y2=[5, 4, 3, 2, 1]


plt.figure(1)
plt.plot(x1, y1, 'b^-', label='legend-label-1')
plt.plot(x2, y2, 'g^-', label='legend-label-2')
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('Plot Title')
plt.legend(loc='best') # 'upper left' 'upper right'
plt.show()
plt.savefig('plot.jpg')
```
![Screenshot](https://github.com/DrUzair/Py/blob/master/images/lineplot.jpg)

# Boxplot
