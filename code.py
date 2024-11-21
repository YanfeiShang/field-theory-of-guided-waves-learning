import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d

# 假设原始列表是这样创建的
def convert_complex(num_str):
    return complex(num_str.replace('E', 'e').replace('i', 'j'))       # 给定一个字符串2.435+3.467E-5i，把它转化为python能够使用的复数形式
df=np.genfromtxt('E:\\desktop\\Lc-Rcfreq.txt',delimiter=None,dtype=str) #导入数据，初始时以字符串导入每个量，分隔符含有tab或空格均可，且两数字间可以有多个分隔符
array = np.vectorize(convert_complex)(df) #作用到数组上把每个位置的字符串转换为复数
array=np.delete(array,2,axis=1)
# 转换为三维数组
reshapearray = array.reshape(6, 5, 3)
x=np.real(array[:,0])
y=np.real(array[:,1])
z=np.real(array[:,2])
xi = np.linspace(np.min(x), np.max(x), 100)  # 生成插值点
yi = np.linspace(np.min(y), np.max(y), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='cubic')  
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(xi, yi, zi, cmap='viridis')
# 设置轴标签
ax2.set_xlabel('Rc')
ax2.set_ylabel('Lc')
ax2.set_zlabel('freq(GHz)')
ax2.set_title('Lc-Rc-freq Plot')
plt.show()


