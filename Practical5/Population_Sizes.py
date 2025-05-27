import matplotlib.pyplot as plt

# Population data
UK_Counties = ['England', 'Wales', 'Northern Ireland', 'Scotland']
uk_countries = [57.11, 3.13, 1.91, 5.45]

Zhejiang_neighboring_provinces = ['Anhui', 'Jiangsu', 'Fujian', 'Jiangxi', 'Shanghai']
zhejiang_neighboring_populations = [65.77, 41.88, 45.28, 61.27, 85.15]

# Sort and print (optional)
print("Sorted UK populations:", sorted(uk_countries))
print("Sorted neighboring province populations:", sorted(zhejiang_neighboring_populations))

# Create a figure with 2 subplots
plt.figure(figsize=(12, 6))  # Wider figure for side-by-side plots

# First pie chart - UK Counties
plt.subplot(1, 2, 1)  # 1 row, 2 cols, plot 1
plt.pie(uk_countries, labels=UK_Counties, autopct='%1.1f%%')
plt.title('Population Distribution of UK Countries')

# Second pie chart - Zhejiang Neighboring Provinces
plt.subplot(1, 2, 2)  # 1 row, 2 cols, plot 2
plt.pie(zhejiang_neighboring_populations, labels=Zhejiang_neighboring_provinces, autopct='%1.1f%%')
plt.title('Population of Zhejiang Neighboring Provinces')

# Display both charts
plt.tight_layout()
plt.show()