import arff
import pandas as pd

# Load ARFF
with open('data/raw/german_credit.arff', 'r') as f:
    dataset = arff.load(f)

# Convert to DataFrame
df = pd.DataFrame(dataset['data'], columns=[attr[0] for attr in dataset['attributes']])

# Save as CSV for later steps
df.to_csv('data/staged/data.csv', index=False)
print("Data ingestion complete. CSV saved to data/staged/data.csv")
