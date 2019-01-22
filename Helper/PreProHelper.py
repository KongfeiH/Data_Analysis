import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import medfilt,filtfilt,wiener,detrend
import cv2
class Data_Feature():
    def __init__(self,Matrix):
        Matrix = Matrix - Matrix[0, :]
        Matrix = self.MatMedfilt(Matrix)
        Matrix = Matrix * (Matrix > 0.5)
        self.Matrix=Matrix
        self.Max=np.max(self.Matrix)
        self.MaxSiteNumber,self.MaxSiteTime=self.MaxSite(self.Matrix)
        self.Hash0,self.Hash1,self.Hash2,self.Hash3=self.STRTOHEX(self.AHash(self.Matrix))
        self.NumTorch=self.NumTorch(self.Matrix)
        self.Sum = self.Sum(self.Matrix)
        self.TimeTorch=self.TimeTorch(self.Matrix)

    def MatMedfilt(self,Matrix):
         for i in range(96):
             Matrix[:, i]=medfilt(Matrix[:,i],3)
         return Matrix

    def print(self):
        print(round(self.Max,2), round(self.MaxSiteNumber,2),round(self.MaxSiteTime,2),self.Hash0,self.Hash1,self.Hash2,self.Hash3,round(self.NumTorch,2),round(self.Sum,2),round(self.TimeTorch,2))

    def NumTorch(self,Matrix):
        return (np.sum(Matrix[75] > 0))
    def Sum(self,Matrix):
        return (np.sum(Matrix[75]))

    def STRTOHEX(self,str):
        data = str
        Hex = np.zeros(4)
        Hex[0] = eval(data[0]) * 8 + eval(data[1]) * 4 + eval(data[2]) * 2 + eval(data[3] * 1)
        Hex[1] = eval(data[4]) * 8 + eval(data[5]) * 4 + eval(data[6]) * 2 + eval(data[7] * 1)
        Hex[2] = eval(data[8]) * 8 + eval(data[9]) * 4 + eval(data[10]) * 2 + eval(data[11] * 1)
        Hex[3] = eval(data[12]) * 8 + eval(data[13]) * 4 + eval(data[14]) * 2 + eval(data[15] * 1)
        return Hex[0],Hex[1],Hex[2],Hex[3]
    def AHash(self,img):

        img=cv2.resize(img[70,:].reshape(8,12),(4,4),interpolation=cv2.INTER_CUBIC)
        #cv2.imshow("Image",img)
        #cv2.waitKey(0)
      #  plt.imshow(img)
       # plt.show()
        #  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = img
        s = 0
        hash_str = ''

        for i in range(4):
            for j in range(4):
                s = s + gray[i, j]

        avg = s / 16

        for i in range(4):
            for j in range(4):
                if gray[i, j] > avg:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    def MaxSite(self,Matrix):
        for i in range(80):
            for j in range(96):
                if Matrix[i,j]==self.Max:
                    return j,i
    def TimeTorch(self,Matrix):
        p=self.MaxSiteTime
        if p==0:
            return 0
        while  0!=Matrix[p-1,self.MaxSiteNumber]:
            p=(p-1)
        return p

    def GetFeature(self):
        return np.array([self.Max, \
                         self.MaxSiteNumber,\
                         self.MaxSiteTime, \
                         self.Hash0,  self.Hash1,  self.Hash2,  self.Hash3,\
                         self.NumTorch,\
                         self.Sum,\
                         self.TimeTorch])





