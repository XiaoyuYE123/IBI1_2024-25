# importing the required libraries
import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# setting the working directory
os.chdir('E:/2024_2025/IBI/IBI1_2024-25/IBI1_2024-25/Practical10')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# print the 3rd column for the first 10 rows
print(dalys_data.iloc[:10, 2])
# defining the mask for the data
# print the 10th year with DALYs data recorded in Afghanistan
mask1 = dalys_data['Year'] == 1999
print('the 10th year with DALYs data recorded in Afghanistan is',dalys_data.loc[mask1, 'DALYs'])

# use boolean to print the DALYs data for the year 1990
mask2 = dalys_data['Year'] == 1990
print(dalys_data.loc[mask2,'DALYs'])

mask3 = dalys_data['Entity'] == 'United Kingdom'
# calculating the mean of DALYs for UK and France
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
plt.title("DALYs in UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
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
    # defining the mask for each year
    mask = dalys_data['Year'] == i
    # calculating the mean of DALYs for each year
    # and appending it to the list
    lis.append(dalys_data.loc[mask, 'DALYs'].mean())
    lis1.append(i)
    # checking if the mean of DALYs for the year is greater than the previous maximum
    if a < dalys_data.loc[mask, 'DALYs'].mean():
        a = dalys_data.loc[mask, 'DALYs'].mean()
        b = i
    else:
        a = a
        b = b
print('DALYs in the year',b,'is the largest one, which is ',max(lis))
# plotting the mean of DALYs for each year
plt.plot(lis1, lis, 'r+')
plt.title("Average DALYs per Year")  
plt.xlabel("Year")                   
plt.ylabel("Average DALYs") 
plt.show()