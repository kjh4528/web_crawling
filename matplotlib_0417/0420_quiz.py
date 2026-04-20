# 0420 matplotlib Quiz

# %% 

import matplotlib.pyplot as plt
import numpy as np

y = [55, 62, 70, 75, 80, 88]
x = np.arange(1,len(y)+1)
plt.plot(x,y)
plt.title('Weekly Learning Score')
plt.xlabel('week')
plt.ylabel('score')
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,8)
plt.plot(x,x*3,'ro-')
plt.xlabel('Period')
plt.ylabel('Count')
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11)
plt.plot(x,x**2)
plt.axis([0,10,0,50])
plt.title('y = x^2')
plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,8)
y = x**2
plt.scatter(x,y,c='green',marker='o')
plt.title("y=x^2 scatter")
plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6)
plt.plot(x,x*2,'b-',label='y=2x')
plt.plot(x,x**2,'r--',label='y=x^2')
plt.legend()
plt.title("Two Functions")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,6)
plt.plot(t,t,'b-',label='y=t')
plt.plot(t,t**2,'r-',label='y=t^2')
plt.plot(t,t**3,'g-',label='y=t^3')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2,7)
plt.plot(x,x*4,'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(2,6)
plt.ylim(8,24)
plt.title("Zoomed Graph")
plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x,y_sin,'r-',label='sin')
plt.plot(x, y_cos, 'b:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.show()
# %%
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(1,2)

x = np.arange(0,6)
ax[0].scatter(x,x**2,c='b',marker='o')
ax[1].plot(x,x*3,c='g')
ax[0].set_title('scatter: y=x^2')
ax[1].set_title('plot:y=3x')
plt.show() 
# %%
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(2,1)
x = np.linspace(0,2*np.pi,100)
ax[0].plot(x,np.sin(x),c='r',ls='--',label='sin')
ax[1].plot(x,np.cos(x),c='b',label='cos')

ax[0].grid()
ax[0].set_title('Sin Function')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].legend()

ax[1].grid()
ax[1].set_title('Cos Function')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].legend()

plt.tight_layout()
fig.savefig('sin_cos_plot.png')
plt.show()

# %%
