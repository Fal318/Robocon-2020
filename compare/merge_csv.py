import pandas as pd

df_arrys = []

for i in range(0, 100):
    try:
        df = pd.read_csv(f"../data/csv/data_{i}.csv")
    except FileNotFoundError:
        continue
    else:
        df_arrys.append(df)
merged__df = pd.DataFrame()
for df in df_arrys:
    merged__df = pd.concat([merged__df, df], axis=1)
print(merged__df)

merged__df.to_csv(
    f"../data/csv/merged.csv", header=False, index=False)
