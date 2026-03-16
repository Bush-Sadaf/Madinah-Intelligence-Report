import pandas as pd

air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

print("Air 2021 sheets:", list(air_2021.keys()))
print("Air 2022 sheets:", list(air_2022.keys()))
print("Air 2023 sheets:", list(air_2023.keys()))
print("Air 2024 sheets:", list(air_2024.keys()))