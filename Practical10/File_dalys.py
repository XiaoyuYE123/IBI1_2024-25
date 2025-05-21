# importing the required libraries
import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# setting the working directory
os.chdir('E:/2024_2025/IBI/IBI1_2024-25/IBI1_2024-25/Practical10')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# defining the mask for the data
mask1 = dalys_data['Year'] == 1999
print('the 10th year with DALYs data recorded in Afghanistan is',dalys_data.loc[mask1, 'DALYs'])
print(dalys_data.iloc[:10,[3]])

mask2 = dalys_data['Year'] == 1990
print(dalys_data.loc[mask2,'DALYs'])

mask3 = dalys_data['Entity'] == 'United Kingdom'
m1 = dalys_data.loc[mask3, 'DALYs'].mean()
mask4 = dalys_data['Entity'] == 'France'
m2 = dalys_data.loc[mask4, 'DALYs'].mean()
# printing the mean of DALYs for UK and France
if m1 > m2:
    print('UK has a higher average DALYs than France')
else:
    print('France has a higher average DALYs than UK')
# plotting the data
plt.plot(dalys_data.loc[mask3, 'Year'], dalys_data.loc[mask3, 'DALYs'], 'b+')
plt.show()

# create the list of years and the mean of DALYs for each year
# and find the year with the maximum mean of DALYs
# and print the year and the maximum mean of DALYs
# and plot the mean of DALYs for each year
a = 0
b = 0
lis = list()
lis1 = list()
for i in range(1990, 2020):
    mask = dalys_data['Year'] == i
    lis.append(dalys_data.loc[mask, 'DALYs'].mean())
    lis1.append(i)
    if a < dalys_data.loc[mask, 'DALYs'].mean():
        a = dalys_data.loc[mask, 'DALYs'].mean()
        b = i
    else:
        a = a
        b = b
print('DALYs in the year',b,'is the largest one, which is ',max(lis))
plt.plot(lis1, lis, 'r+')
plt.show()