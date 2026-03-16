import pandas as pd

# ===== MADINAH AIRPORT PASSENGERS =====
airport_data = {
    'Year' : [2021, 2022, 2023, 2024],
    'Total_Passengers' : [1757979, 6340684, 9423410, 8922292],
    'Domestic_Passengers' : [1273049, 1873688, 2053366, 2752484],
    'International_Passengers' : [484930, 4466996, 7370044, 6169808]
}
df_airport = pd.DataFrame(airport_data)
print("=== Madinah Airport Data ===")
print(df_airport)

# ===== MADINAH UMRAH VISITORS =====
umrah_data = {
    'Year' : [2021, 2022, 2023, 2024],
    'Total_Visitors' : [355236, 1099634, 742540, 1032340],
    'Male_Visitors' : [228179, 742879, 503806, 378194],
    'Female_Visitors' : [127057, 356755, 238734, 654146]
}
df_umrah = pd.DataFrame(umrah_data)
print("\n=== Madinah Umrah Visitors Data ===")
print(df_umrah)

print("\nData Compilation Completed!")

# ===== MONTHLY MADINAH UMRAH DATA =====
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_data = {
    'Month': months,
    '2022': [68696, 86133, 99996, 415724, 94713, 40086, 7311, 100397, 63266, 42756, 41120, 39436],
    '2023': [41223, 40187, 124784, 266530, 68399, 15901, 30555, 51097, 35938, 21514, 26260, 20152],
    '2024': [58449, 57046, 171678, 365374, 97137, 22806, 42469, 70741, 50741, 30485, 36864, 28550]
}
df_monthly = pd.DataFrame(monthly_data)
print("\n=== Monthly Madinah Data ===")
print(df_monthly)