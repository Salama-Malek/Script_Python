import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the file and convert it into a table
df = pd.read_csv('project_data.csv')

# Step 2: Print the unique values in the 'marital_status' column
print(df['marital_status'].unique())

# Step 3: Combine values with the same meaning in 'marital_status' column
df['marital_status'] = df['marital_status'].replace({'Relationship': 'Married'})

# Step 4: Calculate the percentage of people with at least a secondary degree
education_counts = df['educational_level'].value_counts(normalize=True)
percentage_secondary_degree = education_counts[education_counts.index >= 'Secondary'].sum() * 100
print(f"Percentage of people with at least a secondary degree: {percentage_secondary_degree:.2f}%")

# Step 5: Select and sort individuals who are single by annual income
single_individuals = df.loc[df['marital_status'] == 'Single']
sorted_single_income = single_individuals.sort_values('annual_income', ascending=False)
print(sorted_single_income['annual_income'])

# Step 6: Add a new column for the total sum of purchases
df['total_purchases'] = df['online_purchases'] + df['store_purchases']

# Step 7: Categorize the total number of purchases into low, medium, and high
df['purchase_category'] = pd.cut(df['total_purchases'], bins=[0, 10, 20, float('inf')], labels=['Low', 'Medium', 'High'])

# Step 8: Display a pie chart of purchase categories
purchase_counts = df['purchase_category'].value_counts()
purchase_counts.plot(kind='pie', autopct='%1.1f%%', labels=purchase_counts.index)
plt.ylabel('')
plt.title('Purchase Categories')
plt.show()

# Step 9: Group by purchase category and calculate averages
grouped_df = df.groupby('purchase_category').agg({
    'online_purchases': 'mean',
    'store_purchases': 'mean',
    'annual_income': 'mean'
})
print(grouped_df)

# Step 10: Create subplots for education level vs. income and purchases
education_order = ['Basic', 'High School', 'Graduation', 'Master', 'PhD']
education_values = [0, 1, 2, 3, 4]

fig, (ax1, ax2) = plt.subplots(2, 1)

# Subplot 1: Education level vs. income
ax1.scatter(education_values, df.groupby('educational_level')['annual_income'].mean(), c='blue')
ax1.set_xticks(education_values)
ax1.set_xticklabels(education_order)
ax1.set_xlabel('Education Level')
ax1.set_ylabel('Annual Income')
ax1.set_title('Education Level vs. Annual Income')

# Subplot 2: Education level vs. number of purchases
ax2.scatter(education_values, df.groupby('educational_level')['total_purchases'].mean(), c='red')
ax2.set_xticks(education_values)
ax2.set_xticklabels(education_order)
ax2.set_xlabel('Education Level')
ax2.set_ylabel('Number of Purchases')
ax2.set_title('Education Level vs. Number of Purchases')

plt.tight_layout()
plt.show()
