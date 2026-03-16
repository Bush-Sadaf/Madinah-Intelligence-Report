import pandas as pd

# LOAD AIR TRANSPORT FILES
air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

# EXTRACT MADINAH DATA ROW FROM EACH YEAR
df_2021 = air_2021['2']
df_2022 = air_2022['2']
df_2023 = air_2023['3']
df_2024 = air_2024['4']

# SEARCH ADN PRINT MADINAH ROW
for year, df in [('2021', df_2021), ('2022', df_2022), ('2023', df_2023), ('2024', df_2024)]:
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Mohammed|Mohammad', case=False, na=False)
        if mask.any():
            print(f"\n=== Madinah Row - {year} ===")
            print(df[mask].to_string())
            break

# Check which sheet has big passenger numbers for 2023 and 2024
print("\n=== Checking 2023 sheets for big numbers ===")
for sheet_name, df in air_2024.items():
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Mohammed|Mohammad', case=False, na=False)
        if mask.any():
            row = df[mask]
            print(f"Sheet {sheet_name}: {row.values}")