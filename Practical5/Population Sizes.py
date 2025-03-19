import matplotlib.pyplot as plt
UK_Counties = ['England', 'Wales', 'Northern Ireland', 'Scotland']
Zhejiang_neighboring_provinces = ['Anhui', 'Jiangsu', 'Fujian', 'Jiangxi', 'Shanghai']
uk_countries=[57.11,3.13,1.91,5.45]
zhejiang_neighboring_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
print(sorted(uk_countries))
print(sorted(zhejiang_neighboring_provinces))
plt.pie(uk_countries, labels=UK_Counties, autopct='%1.1f%%')
plt.pie(zhejiang_neighboring_provinces, labels=Zhejiang_neighboring_provinces, autopct='%1.1f%%')
plt.show()