import pandas as pd

# LOAD UMRAH FILES
umrah_2022 = pd.read_excel('data/Umrah Statistics2022.xlsx', sheet_name=None)
umrah_2023 = pd.read_excel('data/Umrah Statistics2023.xlsx', sheet_name=None)
umrah24_q1 = pd.read_excel('data/Umrah Statistics Q1 2024.xlsx', sheet_name=None)
umrah24_q2 = pd.read_excel('data/Umrah Statistics Q2 2024.xlsx', sheet_name=None)
umrah24_q3 = pd.read_excel('data/Umrah Statistics Q3 2024.xlsx', sheet_name=None)
umrah24_q4 = pd.read_excel('data/Umrah Statistics Q4 2024.xlsx', sheet_name=None)

# PRINT SHEET 1 OF EACH
for year, data in [('2022', umrah_2022), ('2023', umrah_2023), ('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2), ('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    print(f"\n=== Umrah {year} - Sheet 1 ===")
    print(data['1'].to_string())

umrah_2021 = pd.read_excel('data/Umrah Statistics2021.xlsx', sheet_name=None)
print("Umrah 2021 sheets:", list(umrah_2021.keys()))

# PEEK INSIDE FIRST FEW SHEETS
for sheet in list(umrah_2021.keys())[:5]:
    print(f"\n=== 2021 Sheet {sheet} ===")
    print(umrah_2021[sheet].head(5).to_string())

print("\n=== 2021 Sheet 1 Full ===")
print(umrah_2021['1'].to_string())

# Check sheet 3 of 2022 for Madinah region data
print("\n=== Umrah 2022 - Sheet 3 Full ===")
print(umrah_2022['3'].to_string())

# CHECK ALL FILES FOR MADINAH REGION DATA
for year, data in [('2021', umrah_2021), ('2022', umrah_2022), ('2023', umrah_2023), ('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2),('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    print(f"\n=== {year} - Searching Madinah ===")
    for sheet_name, df in data.items():
        for col in df.columns:
            mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
            if mask.any():
                print(f"Found in sheet: {sheet_name}")
                break

# Check sheet 3 of all 2024 quarters
for quarter, data in [('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2), 
                      ('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    print(f"\n=== {quarter} - Sheet 3 ===")
    print(data['3'].to_string())



# CHECK FEMALE/MALE BREAKDOWN FOR ALL YEARS
# 2021, 2022, 2023
for year, data in [('2022', umrah_2022), ('2023', umrah_2023)]:
    for sheet in ['3-1', '3-2']:
        df = data[sheet]
        for col in df.columns:
            mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
            if mask.any():
                row = df[mask].iloc[0]
                print(f"\n=== {year} Sheet {sheet} - Madinah Row ===")
                print(row.tolist())
                break

# 2024 QUARTERS - SHEET 4 = MALE, SHEET5 = FEMELE
for quarter, data in [('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2), ('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    for sheet in ['4', '5']:
        df = data[sheet]
        for col in df.columns:
            mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
            if mask.any():
                print(f"\n=== {quarter} Sheet {sheet} - Madinah Row ===")
                print(row.tolist())
                break

# 2021 separately because different sheet structure
for sheet, label in [('4-1', 'Male'), ('4-2', 'Female')]:
    df = umrah_2021[sheet]
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
        if mask.any():
            row = df[mask].iloc[0]
            print(f"\n=== 2021 {label} - Madinah Row ===")
            print(row.tolist())
            break

# 2022 and 2023
for year, data in [('2022', umrah_2022), ('2023', umrah_2023)]:
    for sheet, label in [('3-1', 'Male'), ('3-2', 'Female')]:
        df = data[sheet]
        for col in df.columns:
            mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
            if mask.any():
                row = df[mask].iloc[0]
                print(f"\n=== {year} {label} - Madinah Row ===")
                print(row.tolist())
                break

# 2024 quarters
for quarter, data in [('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2),
                      ('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    for sheet, label in [('4', 'Male'), ('5', 'Female')]:
        df = data[sheet]
        for col in df.columns:
            mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
            if mask.any():
                row = df[mask].iloc[0]
                print(f"\n=== {quarter} {label} - Madinah Row ===")
                print(row.tolist())
                break
'''

# Check 2021 sheet names first
print("=====2021 sheets:", list(umrah_2021.keys()))
'''
# Check 2021 sheets for male/female Madinah data
for sheet in ['2', '4', '4-1', '4-2', '5', '5-1', '5-2']:
    df = umrah_2021[sheet]
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
        if mask.any():
            row = df[mask].iloc[0]
            print(f"\n=== 2021 Sheet {sheet} - Madinah Row ===")
            print(row.tolist())
            break


# ===== EXTRACT MONTHLY MADINAH DATA ALL YEARS =====

# 2021
df_2021_monthly = umrah_2021['2']
for col in df_2021_monthly.columns:
    mask = df_2021_monthly[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
    if mask.any():
        row = df_2021_monthly[mask].iloc[0]
        print("\n=== 2021 Monthly Madinah Data ===")
        print(row.tolist())
        break

# 2022
df_2022_monthly = umrah_2022['3']
for col in df_2022_monthly.columns:
    mask = df_2022_monthly[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
    if mask.any():
        row = df_2022_monthly[mask].iloc[0]
        print("\n=== 2022 Monthly Madinah Data ===")
        print(row.tolist())
        break

# 2023
df_2023_monthly = umrah_2023['3']
for col in df_2023_monthly.columns:
    mask = df_2023_monthly[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
    if mask.any():
        row = df_2023_monthly[mask].iloc[0]
        print("\n=== 2023 Monthly Madinah Data ===")
        print(row.tolist())
        break

# 2024 all quarters
for quarter, data in [('Q1 2024', umrah24_q1), ('Q2 2024', umrah24_q2),
                      ('Q3 2024', umrah24_q3), ('Q4 2024', umrah24_q4)]:
    df = data['3']
    for col in df.columns:
        mask = df[col].astype(str).str.contains('Madinah|Madina', case=False, na=False)
        if mask.any():
            row = df[mask].iloc[0]
            print(f"\n=== {quarter} Monthly Madinah Data ===")
            print(row.tolist())
            break