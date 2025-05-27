# Store the popularity of the following programming languages in a dictionary
language_popularity = {
    'JavaScript': 62.3,
    'HTML': 52.9,
    'Python': 51,
    'SQL': 51,
    'TypeScript': 38.5
}

print(language_popularity)

# Variable for activity (language) that can be modified
activity = 'Python'  # You can change this to any language in the dictionary

# Return popularity of the given language
if activity in language_popularity:
    print(f"The popularity of {activity} is {language_popularity[activity]}%.")
else:
    print(f"{activity} is not in the language popularity dictionary.")

# Display the popularity of the programming languages in a bar chart
import matplotlib.pyplot as plt

# Prepare data
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

# Plot bar chart
plt.bar(languages, percentages, color='blue')
plt.xlabel('Programming Languages')
plt.ylabel('Users (%)')
plt.title('Programming Language Popularity')

# Highlight the selected activity in red if it exists
if activity in language_popularity:
    index = languages.index(activity)
    plt.bar(languages[index], percentages[index], color='red')  # Overplot in red

plt.show()
