import pandas as pd

# Load the staged CSV
df = pd.read_csv('data/staged/data.csv')

print("🔎 Dataset Overview:")
print(df.head())

print("\n📊 Shape of the dataset:", df.shape)

print("\n❓ Missing values per column:")
print(df.isnull().sum())

print("\n🧬 Data types:")
print(df.dtypes)
