#store the popularity of the following programming languages in a dictionary
language_popularity = {'JavaScript':62.3, 'HTML':52.9, 'Python':51,'SQL':51, 'TypeScript':38.5}
print(language_popularity)
#display the popularity of the programming languages in a bar chart
#first，import the matplotlib library
#second, create a list of the programming languages and a list of the popularity percentages
#third, use the bar() function to create a bar chart
#fourth, add labels and a title to the bar chart
import matplotlib.pyplot as plt
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())
plt.bar(languages, percentages, color='blue')
plt.xlabel('Programming Languages')
plt.ylabel('Users(%)')
plt.title('Programming Language Popularity')
plt.show()