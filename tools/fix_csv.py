import pandas as pd

df = pd.read_csv("../data/csv/data.csv")
fixed_df = pd.DataFrame()
line_name = [["小節", ""]]
for old_line, new_line in line_name:
    fixed_df[new_line] = df[old_line]
for row in df[""]:
    pass
