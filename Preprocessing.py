import numpy as np
import matplotlib.pyplot as plt
from Helper import Filter as F

RAW_DATA__CSV = r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\9.csv"
data1=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\1.csv","rb"),delimiter=",",skiprows=0)
data2=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\2.csv","rb"),delimiter=",",skiprows=0)
data3=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\3.csv","rb"),delimiter=",",skiprows=0)
data4=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\4.csv","rb"),delimiter=",",skiprows=0)
data5=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\1.csv","rb"),delimiter=",",skiprows=0)
data6=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\2.csv","rb"),delimiter=",",skiprows=0)
data7=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\3.csv","rb"),delimiter=",",skiprows=0)
data8=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\4.csv","rb"),delimiter=",",skiprows=0)
data9=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\5.csv", "rb"), delimiter=",", skiprows=0)


plt.subplot(331)
plt.plot(F.filter(data1).Matrix)
plt.subplot(332)
plt.plot(F.filter(data2).Matrix)
plt.subplot(333)
plt.plot(F.filter(data3).Matrix)
plt.subplot(334)
plt.plot(F.filter(data4).Matrix)
plt.subplot(335)
plt.plot(F.filter(data5).Matrix)
plt.subplot(336)
plt.plot(F.filter(data6).Matrix)
plt.subplot(337)
plt.plot(F.filter(data7).Matrix)
plt.subplot(338)
plt.plot(F.filter(data8).Matrix)
plt.subplot(339)
plt.plot(F.filter(data9).Matrix)
plt.show()


# F.filter(data1).print()
# F.filter(data2).print()
# F.filter(data3).print()
# F.filter(data4).print()
# F.filter(data5).print()
# F.filter(data6).print()
# F.filter(data7).print()
# F.filter(data8).print()
# F.filter(data9).print()



