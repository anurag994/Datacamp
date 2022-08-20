#1 List of words to pair with products
words = ['buy','price','discount','promotion','promo','shop']

# Print list of words
print(words)

#2 Combine the words with the product names
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

#3 Convert the list into a DataFrame
# Load library
import pandas as pd

# Create a DataFrame from list
keywords_df = pd.DataFrame(keywords_list)

# Print the keywords DataFrame to explore it
print(keywords_df.head())

#4 Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0:'Ad Group',1:'Keyword'})

#5 Add a campaign column
keywords_df['Campaign']='SEM_Sofas'

#6 Add a criterion type column
keywords_df['Criterion Type']='Exact'

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

#7 Change criterion type match to phrase

keywords_df['Criterion Type']='Phrase'
# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)

#8 Save the final keywords to a CSV file

keywords_df_final.to_csv('keywords.csv', index=False)

# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
