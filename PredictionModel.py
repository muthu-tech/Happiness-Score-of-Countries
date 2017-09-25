# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:53:54 2017

@author: muthu
"""
from __future__ import division
import numpy as np
import pandas as py
import math
from sklearn import linear_model
# Loading the  dataset as training and testing
dataFrame = py.read_csv('C:/Users/muthu/Desktop/Data/Training/TrainingDataWithNearestMean.csv')
testFrame = py.read_csv('C:/Users/muthu/Desktop/Data/Test/TestWithNearestMean.csv')

#Using the features
xtraining = dataFrame[['android_total_ratings','android_average_rating','ios_current_ratings','ios_file_size']].as_matrix()
xtest = testFrame[['android_total_ratings','android_average_rating','ios_current_ratings','ios_file_size']].as_matrix()

# Splitting the targets into training/testing sets
ytrain = dataFrame[['ios_all_ratings']].values

# Creating linear regression object
linearReg = linear_model.LinearRegression()

#To validate the model, lets gather the actual Y values
ytest = testFrame[['ios_all_ratings']].values
# Train the model using the training sets
linearReg.fit(xtraining, ytrain)
#predict the target
linear_predictedList = linearReg.predict(xtest)


# Ridge
from sklearn.linear_model import Ridge
clf = Ridge(alpha=0.5)
clf.fit(xtraining, ytrain)
ridge_predictedList =clf.predict(xtest)
print type(ridge_predictedList)
#Lasso
from sklearn import linear_model
clfLasso = linear_model.Lasso(alpha=0.5)
clfLasso.fit(xtraining, ytrain)
lasso_predictedList = clfLasso.predict(xtest)
#print lasso_predictedList.tolist()

#r = ridge_predictedList.tolist()
#print ridge_predictedList[0]
def model_evaluation(predictedList, ytest):
    predicted_list = []
    actual_list = []   
    correct = 0
    numpyArrayList = predictedList.tolist()
    numpyActual = ytest.tolist()
    for item1 in numpyActual:
        actual_list.append(item1[0])
    if type(numpyArrayList[0]) == type(list):
        for item in numpyArrayList:
            predicted_list.append(item[0])

    else:
        predicted_list = numpyArrayList
    print len(predicted_list) 
    print len(actual_list)
    for i in range(len(predicted_list)):
        if predicted_list[i] == actual_list[i]:
            correct += 1
            print predicted_list[i]
    acc = correct / len(predicted_list)
    msr = np.mean((predictedList - ytest) ** 2)
    error = math.sqrt(msr)
    normalisedError = error/(max(actual_list)-min(actual_list))
    return acc,error,normalisedError

linearaccuracy , linearError, linearNormalised = model_evaluation(linear_predictedList,ytest)
ridgeaccuracy, ridgeError, ridgeNormalised = model_evaluation(ridge_predictedList,ytest)
lassoaccuracy , lassoError,lassoNormalised = model_evaluation(lasso_predictedList,ytest)
#==============================================================================
toExcel ={}
toExcel.update({'LineariOS':{'number of correct predictions':linearaccuracy,
                       'root mean squared error':linearError,
                       'NormalisedRMS Error':linearNormalised}})
toExcel.update({'LassoiOS':{'number of correct predictions':lassoaccuracy,
                       'root mean squared error':lassoError,
                       'NormalisedRMS Error':lassoNormalised}})
toExcel.update({'RidgeiOS':{'number of correct predictions':ridgeaccuracy,
                       'root mean squared error':ridgeError,
                       'NormalisedRMS Error':ridgeNormalised}})
panda = py.DataFrame(toExcel)
tpanda = panda.transpose()
tpanda.to_excel("NearestMeanEvaluation/0.5iOS3rdValidation.xlsx")

# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % androidregr.score(xtest, ytest))
#print len(regr.predict(xtest))
#print len(xtest)
# Plot outputs
#plt.scatter(xtest, ytest,  color='black')
#plt.plot(xtest, regr.predict(xtest), color='blue',
#         linewidth=3)

#==============================================================================
# plt.xticks(())
# plt.yticks(())
# 
# plt.show()
#==============================================================================


# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % clf.score(xtest, ytest))




#print("Mean squared error: %.2f"
      #% np.mean((clfLasso.predict(xtest) - ytest) ** 2))
# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % clfLasso.score(xtest, ytest))
