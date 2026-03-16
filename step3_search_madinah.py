import pandas as pd

air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

for year, data in [('2021', air_2021), ('2022', air_2022), ('2023', air_2023), ('2024', air_2024)]:
    print(f"\n=== Searching Madinah in {year} ===")
    for sheet_name, df in data.items():
        for col in df.columns:
            if df[col].astype(str).str.contains('Madinah|Madina|Mohammad|Mohammed', case=False, na=False).any():
                print(f"  Found in sheet: {sheet_name}, column: {col}")
                break