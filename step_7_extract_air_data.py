import pandas as pd

# LOAD AIR TRANSPORT FILES
air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

# EXTRACT CORRECT SHEETS
df_2021 = air_2021['2']
df_2022 = air_2022['2']
df_2023 = air_2023['1']
df_2024 = air_2024['3']

# FIND MADINAH ROW IN EACH YEAR
def get_madinah_total(df, year):
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Mohammed|Mohammad', case=False, na=False)
        if mask.any():
            row = df[mask].iloc[0]
            numbers = []
            for val in row:
                try:
                    numbers.append(float(str(val).replace(',', '')))
                except:
                    pass
            print(f"\n=== {year} Madinah Numbers ===")
            print(numbers)
            return numbers
        
get_madinah_total(df_2021, '2021')
get_madinah_total(df_2022, '2022')
get_madinah_total(df_2023, '2023')
get_madinah_total(df_2024, '2024')

for year, df in [('2021', df_2021), ('2022', df_2022), ('2023', df_2023), ('2024', df_2024)]:
    print(f"\n=== {year} Column Headers adn Madinah Values ===")
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Mohammed|Mohammad', case=False, na=False)
        if mask.any():
            row = df[mask].iloc[0]
            for c, v in zip(df.columns, row):
                print(f"{c} -> {v}")
            break

print("\n=== 2021 Sheet 2 Full Data ===")
print(air_2021['2'].to_string())

print("\n=== 2023 Sheet 1 Full Data ===")
print(air_2023['1'].to_string())

print("\n=== 2024 Sheet 3 Full Data ===")
print(air_2024['3'].to_string())

print("\n=== 2024 Sheet 6 Full Data ===")
print(air_2024['6'].to_string())