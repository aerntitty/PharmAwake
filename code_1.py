import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'cause_of_deaths.csv'
data = pd.read_csv(file_path)


# Filter the dataset for the relevant columns
columns_of_interest = [
    'Country/Territory', 'Year', 'Drug Use Disorders', 'Cardiovascular Diseases', 
    'Neoplasms', 'Diabetes Mellitus', 'Chronic Respiratory Diseases'
]
filtered_data = data[columns_of_interest]
filtered_data['Year'] = pd.to_datetime(filtered_data['Year'], format='%Y')
filtered_data['Drug Use Disorders'] *=1000 # Multiply by 1000 to get a better scale

# Group by year and sum the deaths for each cause
grouped_data = filtered_data.groupby('Year').sum().reset_index()

# Plot the data
plt.figure(figsize=(14, 8))
plt.plot(grouped_data['Year'], grouped_data['Drug Use Disorders'], label='Drug Use Disorders', marker='o')
plt.plot(grouped_data['Year'], grouped_data['Cardiovascular Diseases'], label='Cardiovascular Diseases', marker='o')
plt.plot(grouped_data['Year'], grouped_data['Neoplasms'], label='Neoplasms', marker='o')
plt.plot(grouped_data['Year'], grouped_data['Diabetes Mellitus'], label='Diabetes Mellitus', marker='o')
plt.plot(grouped_data['Year'], grouped_data['Chronic Respiratory Diseases'], label='Chronic Respiratory Diseases', marker='o')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Deaths Related to Drug Use Disorders vs Other Causes Over the Years')
plt.legend()
plt.grid(True)
plt.show()

year = 2019
year_data = filtered_data[filtered_data['Year'] == year]

# Group by country and sum the deaths for each cause
grouped_data = year_data.groupby('Country/Territory').sum().reset_index()

# Plot the data
causes = ['Drug Use Disorders', 'Cardiovascular Diseases', 'Neoplasms', 'Diabetes Mellitus', 'Chronic Respiratory Diseases']
for cause in causes:
    plt.figure(figsize=(14, 8))
    plt.bar(grouped_data['Country/Territory'], grouped_data[cause])
    plt.xlabel('Country/Territory')
    plt.ylabel('Number of Deaths')
    plt.title(f'Deaths from {cause} in {year}')
    plt.xticks(rotation=90)
    plt.show()
