##  Python SCRIPT: EmployeeDiscovery.py
## 
##  Description:  Sample Code Python Tutorial - LocalFile
##                
## 
##  Parameters : None
##
##  License:  
##
##  Repository: 
## 
##  Documentation: In the code

##
##
##  Date				    Developer		  	Action
##  ---------------------------------------------------------------------
##  Jan 15, 2019    		Steve Young			Inital development 
## 
## 
## 
## 
## 


#%%
import matplotlib.pyplot as plt
import numpy as nump

x = [3,4,6,3,4,3,8,9,7,8,]    # Create a list of numbers
plt.plot(x)       # Plot the sine of each x point
plt.show()                   # Display the plot
 
#%%
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as pp



#%%
Employees = pd.read_csv(r'C:\Users\steveyoung\Documents\GitHub\PythonTutorial\Excel_PowerBI_StarterDataSet_2019_Mini_v1.csv')

#%%
#Clean UP

Employees_trimmed = Employees.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


#%%
#give me a good description and initial analysis of my data
Employees.describe()
Employees.columns
#%%
#distribution 
Employees['GrossPay'].hist(bins=50)
Employees.boxplot(column='GrossPay')
Employees.boxplot(column='GrossPay', by = 'MaritalStatus')
Employees.boxplot(column='GrossPay', by = 'Gender')

#%%
Employees

#%%
Employees.index


#%%
Employees.loc[0]


#%%
Employees.set_index('NameFull',inplace=True)
Employees_trimmed.set_index('NameFull',inplace=True)
#%%
Employees.loc[' Ashley Berry']

#%%
Employees_trimmed.loc['Ashley Berry']
#%%
Employees


#%%
Employees.info()


#%%
len(Employees)


#%%
Employees.columns


#%%
pd.to_datetime(Employees.HireDate)


#%%
#give me a good description and initial analysis of my data
Employees

#%%
#give me a good description and initial analysis of my data
Employees.describe()
#%%
Employees['GrossPay'].hist(bins=50)
#%%
pp.hist(Employees['GrossPay'], color = "skyblue", ec="skyblue", bins=50, )

#%%
#loandata['ApplicantIncome'].hist(by=df['Letter'])
Employees['GrossPay'].plot(kind='box', figsize=[16,8])
#%%
Employees.boxplot(column='GrossPay')
Employees.boxplot(column='GrossPay', by = 'JobTitle')




