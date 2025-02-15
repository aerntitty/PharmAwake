import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/Users/beckyiyeh/Documents/PharmAwake/cause_of_deaths.csv'
data = pd.read_csv(file_path)

# Filter the dataset for the relevant columns
columns_of_interest = [
    'Country/Territory', 'Year', 'Drug Use Disorders', 'Cardiovascular Diseases', 
    'Neoplasms', 'Diabetes Mellitus', 'Chronic Respiratory Diseases'
]
filtered_data = data[columns_of_interest]

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
