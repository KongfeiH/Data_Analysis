import numpy as np
import matplotlib.pyplot as plt
from Helper import PreProHelper as F

# RAW_DATA__CSV = r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\9.csv"
# data1=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\1.csv","rb"),delimiter=",",skiprows=0)
# data2=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\2.csv","rb"),delimiter=",",skiprows=0)
# data3=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\3.csv","rb"),delimiter=",",skiprows=0)
# data4=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\怡宝矿泉水瓶\4.csv","rb"),delimiter=",",skiprows=0)
# data5=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\1.csv","rb"),delimiter=",",skiprows=0)
# data6=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\2.csv","rb"),delimiter=",",skiprows=0)
# data7=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\3.csv","rb"),delimiter=",",skiprows=0)
# data8=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\4.csv","rb"),delimiter=",",skiprows=0)
# data9=np.loadtxt(open(r"E:\OneDrive\Python\Data_Analysis\Raw Data\柚子\5.csv", "rb"), delimiter=",", skiprows=0)
#
#
# plt.subplot(331)
# plt.plot(F.Data_Feature(data1).Matrix)
# plt.subplot(332)
# plt.plot(F.Data_Feature(data2).Matrix)
# plt.subplot(333)
# plt.plot(F.Data_Feature(data3).Matrix)
# plt.subplot(334)
# plt.plot(F.Data_Feature(data4).Matrix)
# plt.subplot(335)
# plt.plot(F.Data_Feature(data5).Matrix)
# plt.subplot(336)
# plt.plot(F.Data_Feature(data6).Matrix)
# plt.subplot(337)
# plt.plot(F.Data_Feature(data7).Matrix)
# plt.subplot(338)
# plt.plot(F.Data_Feature(data8).Matrix)
# plt.subplot(339)
# plt.plot(F.Data_Feature(data9).Matrix)
# plt.show()
#
#
# F.Data_Feature(data1).print()
# F.Data_Feature(data2).print()
# F.Data_Feature(data3).print()
# F.Data_Feature(data4).print()
# F.Data_Feature(data5).print()
# F.Data_Feature(data6).print()
# F.Data_Feature(data7).print()
# F.Data_Feature(data8).print()
# F.Data_Feature(data9).print()

# RAW_DATA__CSV = r"E:\OneDrive\Python\Data_Analysis\Raw Data\姿态\塑料圆柱体\\"
# PreDataName="塑料圆柱体"
# Feature=np.zeros((50,10))
# for i in range(50):
#     data=np.loadtxt(open(RAW_DATA__CSV+str(i+1)+".csv","rb"),delimiter=",",skiprows=0)
#     Feature[i,:]= F.Data_Feature(data).GetFeature()
# print(Feature)
# np.savetxt("E:\OneDrive\Python\Data_Analysis\Pre Data\姿态\\"+PreDataName+".csv", Feature, delimiter=',')







