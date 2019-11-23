import numpy as np
import matplotlib.pyplot as plt

'''x = [np.random.randn() for i in range(10)]
y = [np.random.randn() for i in range(10)]
z = [np.random.randn() for i in range(10)]
plt.plot(x, label="alpha 1")
plt.plot(y, label="alpha 2")
plt.plot(z, label="alpha 3")
plt.subplot(321)
plt.plot(x, label="alpha 1")
plt.subplot(322)
plt.plot(y, label="alpha 2")
plt.subplot(313)
plt.plot(z, label="alpha 3")
plt.legend()
plt.show()'''
#-------------------------------

x=[4,2,2,4,3]
y=["a","b","c","d","e"]
plt.pie(x,
        startangle=90,
        shadow=True,
        explode=(0,0,0.1,0,0.2),
        autopct="%1.1f%%"
        )
plt.legend()
plt.title("First")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")