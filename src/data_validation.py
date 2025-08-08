import pandas as pd

df = pd.read_csv('data/staged/data.csv')

with open("validation_output.txt", "w", encoding="utf-8") as f:
    f.write("🔎 Dataset Overview:\n")
    f.write(df.head().to_string())
    f.write("\n\n📊 Shape of the dataset:\n")
    f.write(str(df.shape))
    f.write("\n\n❓ Missing values per column:\n")
    f.write(df.isnull().sum().to_string())
    f.write("\n\n🧬 Data types:\n")
    f.write(df.dtypes.to_string())

print("✅ Data validation output saved to validation_output.txt")
