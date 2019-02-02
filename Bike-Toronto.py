
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#defining directory
os.chdir('C:/Users/LM 617/Desktop/')

#reading the csv file

Q1=pd.read_csv('Bikeshare Ridership (2017 Q1).csv',low_memory=False)
Q2=pd.read_csv('Bikeshare Ridership (2017 Q2).csv',low_memory=False)
Q3=pd.read_csv('Bikeshare Ridership (2017 Q3).csv',low_memory=False)

Q1_use=Q1.shape[0]
Q2_use=Q2.shape[0]
Q3_use=Q3.shape[0]

objects = ('Q1', 'Q2', 'Q3')
y_pos = np.arange(len(objects))
period = [Q1_use/100000,Q2_use/100000,Q3_use/100000]


 
plt.bar(y_pos, period , align='center', alpha=0.5, color='r')
plt.xticks(y_pos, objects)
plt.ylabel('Usage(*10^5)')
plt.xlabel('Period')
plt.title('Population of Bike Share users')

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=1.0
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)

plt.show()


# frequency of each event can be saved in a new df called freq
#freq=data['INCIDENT_TYPE_DESC'].value_counts()

#inc_sum=freq.sum()
#print('all the inciddent are:',inc_sum)
#Question 1 proportion of most common response

#print('proportion of most common response is:',freq.max()/inc_sum)

#Question 2 units on the scene
#build_fire=data.loc[data['INCIDENT_TYPE_DESC'] == '111 - Building fire']
#smoke=data.loc[data['INCIDENT_TYPE_DESC'] == '651 - Smoke scare, odor of smoke']

#mean_units_build=build_fire['UNITS_ONSCENE'].mean()
#mean_units_smoke=smoke['UNITS_ONSCENE'].mean()

#print('ratio of mean is:', mean_units_build/mean_units_smoke)

#Question 3 false call

#false=data.loc[data['INCIDENT_TYPE_DESC'] == '710 - Malicious, mischievous false call, other']

#fals_cals=false['BOROUGH_DESC'].value_counts()
#print(fals_cals)
#print(fals_cals.keys())

#All data inputs are for period of 2013 to 2017, ratio of rate of false calls over 4 years is equal to ratio of falls calls

#print('ratio of false calls are:', fals_cals['1 - Manhattan']/fals_cals['3 - Staten Island'])


#Question 4


