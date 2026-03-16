import pandas as pd

# LOAD UMRAH FILES
umrah_2021 = pd.read_excel('data/Umrah Statistics2021.xlsx', sheet_name=None)
umrah_2022 = pd.read_excel('data/Umrah Statistics2022.xlsx', sheet_name=None)
umrah_2023 = pd.read_excel('data/Umrah Statistics2023.xlsx', sheet_name=None)
umrah24_q1 = pd.read_excel('data/Umrah Statistics Q1 2024.xlsx', sheet_name=None)
umrah24_q2 = pd.read_excel('data/Umrah Statistics Q2 2024.xlsx', sheet_name=None)
umrah24_q3 = pd.read_excel('data/Umrah Statistics Q3 2024.xlsx', sheet_name=None)
umrah24_q4 = pd.read_excel('data/Umrah Statistics Q4 2024.xlsx', sheet_name=None)

# CHECK SHEET NAMES
print("Umrah 2021 sheets:", list(umrah_2021.keys()))
print("Umrah 2022 sheets:", list(umrah_2022.keys()))
print("Umrah 2023 sheets:", list(umrah_2023.keys()))
print("Umrah Q1 2024 sheets:", list(umrah24_q1.keys()))

print("\nAll Umrah files loaded")

# Peek inside sheet 1 of all years
print("\n=== Umrah 2021 - Sheet 1 ===")
print(umrah_2021['1'].head(10).to_string())

print("\n=== Umrah 2022 - Sheet 1 ===")
print(umrah_2022['1'].head(10).to_string())

print("\n=== Umrah 2023 - Sheet 1 ===")
print(umrah_2023['1'].head(10).to_string())

print("\n=== Umrah Q1 2024 - Sheet 1 ===")
print(umrah24_q1['1'].head(10).to_string())

print("\n=== Checking ALL 2021 sheets for Madinah ===")

print("\n=== Umrah ALL YEARS - All sheets peek ===")

for year, data in [('2021', umrah_2021), ('2022', umrah_2022), ('2023', umrah_2023), ('Q1 2024', umrah24_q1)]:
    print(f"\n{'='*20} {year} {'='*20}")
    for sheet_name, df in data.items():
        print(f"\nSheet {sheet_name}:")
        print(df.head(5).to_string())