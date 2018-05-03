# Line Plot
```python
import matplotlib
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(x1, y1, 'b^-', label='legend-label-1')
plt.plot(x2, y2, 'b^-', label='legend-label-2')
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('Plot Title')
plt.savefig('path/to/file.jpg')
```
