# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import os
sns.set()
os.getcwd()


# %%
rawDataPass = pd.read_excel('source\\convertedData\\rawDataCleaned\\XLSX/Passed.xlsx')

rawDataPass['Admitted'] = 1
rawDataPass


# %%
rawDataFail = pd.read_excel('source\\convertedData\\rawDataCleaned\\XLSX/Failed.xlsx')

rawDataFail['Admitted'] = 0
rawDataFail


# %%
data = pd.concat([rawDataPass, rawDataFail])
data

# %% [markdown]
# #### Building the regression 

# %%
y = data['Admitted'] # dependent variable
x1 = data['Points'] # independent variable


# %%
x = sm.add_constant(x1)
regLog = sm.Logit(y,x)
resultsLog = regLog.fit()


# %%
resultsLog.summary()

# %% [markdown]
# #### Predicting

# %%
resultsLog.predict()


# %%
np.array(data['Admitted'])


# %%
cmdf = pd.DataFrame(resultsLog.pred_table())
cmdf.columns = ['Predicted 0', 'Predicted 1']
cmdf = cmdf.rename(index={0:'Actual 0', 1:'Actual 1'})
cmdf
# confusion matrix


# %%
# 71 observations the model predicted 0 and it was 0
# 109 observations the model predicted 0 and it was 1
# 336 observations the model predicted 1 and it was 1
# 39 observations the model predicted 1 and it was 0

# %% [markdown]
# #### Testing

# %%
test = pd.read_excel('source\\testingData\\testing.xlsx')
test


# %%
testActual = test['Admitted']
testData = test.drop(['Admitted'], axis=1)
testData = sm.add_constant(testData)
testData


# %%
def ConfusionMatrix(data, actualValues, model):
    predValues = model.predict(data)
    bins = np.array([0, 0.5, 1])
    cm = np.histogram2d(actualValues, predValues, bins = bins)[0]
    accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
    return cm, accuracy


# %%
cm = ConfusionMatrix(testData, testActual, resultsLog)
cm


# %%



