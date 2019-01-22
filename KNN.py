import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

TrainData=np.loadtxt(open("E:\OneDrive\Python\Data_Analysis\Final Data\Train30.csv","rb"),delimiter=",",skiprows=0)
TestData=np.loadtxt(open("E:\OneDrive\Python\Data_Analysis\Final Data\Test20.csv","rb"),delimiter=",",skiprows=0)


scaler = MinMaxScaler(feature_range=(0,1))
TrainStandard = scaler.fit_transform(TrainData[:,1:])
TestStandard  = scaler.transform(TestData[:,1:])



KNN = KNeighborsClassifier()
KNN.fit(TrainStandard,TrainData[:,0].astype("int"))


KNN_predict = KNN.predict(TestStandard)
print(KNN_predict)
print(TestData[:,0])
def getAccuracy(testSet,predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x] == predictions[x]:
            correct=1+correct
    return correct/200



print(getAccuracy(TestData[:,0],KNN_predict))

