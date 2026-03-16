# ===== STEP 1 - IMPORT LIBRARIES & LOAD FILES =====

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully!")

# ---- AIR TRANSPORT DATA ----
air_2021 = pd.read_excel('data/Air Transport 2021.xlsx', sheet_name=None)
air_2022 = pd.read_excel('data/Air Transport 2022.xlsx', sheet_name=None)
air_2023 = pd.read_excel('data/Air Transport 2023.xlsx', sheet_name=None)
air_2024 = pd.read_excel('data/Air Transport 2024.xlsx', sheet_name=None)

# ---- UMRAH DATA ----
umrah_2021 = pd.read_excel('data/Umrah Statistics2021.xlsx', sheet_name=None)
umrah_2022 = pd.read_excel('data/Umrah Statistics2022.xlsx', sheet_name=None)
umrah_2023 = pd.read_excel('data/Umrah Statistics2023.xlsx', sheet_name=None)
umrah_q1 = pd.read_excel('data/Umrah Statistics Q1 2024.xlsx', sheet_name=None)
umrah_q2 = pd.read_excel('data/Umrah Statistics Q2 2024.xlsx', sheet_name=None)
umrah_q3 = pd.read_excel('data/Umrah Statistics Q3 2024.xlsx', sheet_name=None)
umrah_q4 = pd.read_excel('data/Umrah Statistics Q4 2024.xlsx', sheet_name=None)

print("All 11 files loaded successfully!")