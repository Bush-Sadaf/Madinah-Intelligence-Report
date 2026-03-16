import pandas as pd

#LOAD AIR TRANSPORT FILES
air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

# PEEK INSIDE SHEET 2 OF 2021
print("=== AIR 2021 - Sheet 2 ===")
print(air_2021['2'].to_string())

print("\n=== AIR 2022 - Sheet 2 ===")
print(air_2022['2'].to_string())

print("\n=== AIR 2023 -sheet 3 ===")
print(air_2023['3'].to_string())

print("\n=== AIR 2024 - Sheet 4 ===")
print(air_2024['4'].to_string())