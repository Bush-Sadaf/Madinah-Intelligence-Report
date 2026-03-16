import pandas as pd
import matplotlib.pyplot as plt

# ===== DATA =====
airport_data = {
    'Year': [2021, 2022, 2023, 2024],
    'Total_Passengers': [1757979, 6340684, 9423410, 8922292],
    'Domestic_Passengers': [1273049, 1873688, 2053366, 2752484],
    'International_Passengers': [484930, 4466996, 7370044, 6169808]
}
df_airport = pd.DataFrame(airport_data)

umrah_data = {
    'Year': [2021, 2022, 2023, 2024],
    'Total_Visitors': [355236, 1099634, 742540, 1032340],
    'Male_Visitors': [228179, 742879, 503806, 378194],
    'Female_Visitors': [127057, 356755, 238734, 654146]
}
df_umrah = pd.DataFrame(umrah_data)


# ===== CHART 1 - AIRPORT TOTAL PASSENGERS =====
plt.figure(figsize=(10, 6))
plt.bar(df_airport['Year'], df_airport['Total_Passengers'],
        color=['#d4a843', '#2d6a4f', '#1e3a5f', '#c1440e'])

plt.title('Madinah Airport - Total Passengers 2021-2024', fontsize=16)

plt.xlabel('Year')
plt.ylabel('Total Passengers')
plt.xticks([2021, 2022, 2023, 2024])

for i, v in enumerate(df_airport['Total_Passengers']):
    plt.text(df_airport['Year'][i], v + 100000, f'{v}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('charts/Chart1_airport_total.png', dpi=150)
plt.show()
print("Chart 1 Saved!")




# ===== CHART 2 - DOMESTIC VS INTERNATIONAL PASSENGERS =====

fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35
x =range(len(df_airport['Year']))

bars1 = ax.bar([i - width/2 for i in x], df_airport['Domestic_Passengers'],
               width, label='Domestic', color='#2d6a4f')
bars2 = ax.bar([i + width/2 for i in x], df_airport['International_Passengers'],
               width, label='International', color='#1e3a5f')

ax.set_title('Madinah Airport - Domestic vs International Passengers 2021-2024', fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Passengers')
ax.set_xticks(list(x))
ax.set_xticklabels(df_airport['Year'])
ax.legend()

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100000,
            f'{int(bar.get_height()):,}', ha='center', fontsize=8)
    
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100000,
            f'{int(bar.get_height()):,}', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('charts/charts2_doemstic_vs_international.png', dpi=150)
plt.show()
print("Chart 2 saved!")




# ===== CHART 3 - UMRAH TOTAL VISISTORS TREND =====
plt.figure(figsize=(10, 6))
plt.plot(df_umrah['Year'], df_umrah['Total_Visitors'],
         marker='o', linewidth=2.5, color='#1e3a5f', markersize=8)

for i, v in enumerate(df_umrah['Total_Visitors']):
    plt.text(df_umrah['Year'][i], v + 20000, f'{v: ,}', ha='center', fontsize=9)

plt.title('Madinah - Internal Umrah Visitors Trend 2021-2024', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Total Visitors')
plt.xticks([2021, 2022, 2023, 2024])
plt.grid(axis='y', linestyle='--',alpha=0.7)

plt.tight_layout()
plt.savefig('charts/chart3_umrah_trend.png', dpi=150)
plt.show()
print("Chart 3 Saves!")




# ===== CHART 4 - MALE vs FEMALE UMRAH VISITORS =====
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.35
x = range(len(df_umrah['Year']))

bars1 = ax.bar([i - width/2 for i in x], df_umrah['Male_Visitors'],
               width, label='Male', color='#1e3a5f')
bars2 = ax.bar([i + width/2 for i in x], df_umrah['Female_Visitors'],
               width, label='Female', color='#c1440e')

ax.set_title('Madinah — Male vs Female Umrah Visitors 2021-2024', fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Visitors')
ax.set_xticks(list(x))
ax.set_xticklabels(df_umrah['Year'])
ax.legend()

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
            f'{int(bar.get_height()):,}', ha='center', fontsize=8)
    
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
            f'{int(bar.get_height()):,}', ha='center', fontsize=8)
    
plt.tight_layout()
plt.savefig('charts/chart4_male_vs_female.png', dpi=150)
plt.show()
print("Chart 4 saved!")




# ===== CHART 5 - AIRPORT PASSENGERS vs UMRAH VISITORS COMBINED =====
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(df_airport['Year'], df_airport['Total_Passengers'],
         marker='o', linewidth=2.5, color='#1e3a5f',
         markersize=8, label='Airport Passenger')
ax1.set_xlabel('Year')
ax1.set_ylabel('Airport Passengers', color='#1e3a5f')
ax1.tick_params(axis='y', labelcolor='#1e3a5f')

ax2 = ax1.twinx()
ax2.plot(df_umrah['Year'], df_umrah['Total_Visitors'],
         marker='s', linewidth=2.5, color='#c1440e',
         markersize=8, label='Umrah Visitors')
ax2.set_ylabel('Umrah Visitors', color='#c1440e')
ax2.tick_params(axis='y', labelcolor='#c1440e')

plt.title('Madinah - Airport Passengers vs Umrah Visitors 2021-2024', fontsize=14)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.xticks([2021, 2022, 2023, 2024])
plt.tight_layout()
plt.savefig('charts/chart5_combined.png', dpi=150)
plt.show()
print("Charts 5 saved!")


# ===== MONTHLY DATA =====
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_data = {
    'Month': months,
    '2022': [68696, 86133, 99996, 415724, 94713, 40086, 7311, 100397, 63266, 42756, 41120, 39436],
    '2023': [41223, 40187, 124784, 266530, 68399, 15901, 30555, 51097, 35938, 21514, 26260, 20152],
    '2024': [58449, 57046, 171678, 365374, 97137, 22806, 42469, 70741, 50741, 30485, 36864, 28550]
}
df_monthly = pd.DataFrame(monthly_data)

# ===== CHART 6 - Monthly Peak Analysis =====
plt.figure(figsize=(12, 6))
plt.plot(months, df_monthly['2022'], marker='o', linewidth=2,
         color='#1e3a5f', label='2022')
plt.plot(months, df_monthly['2023'], marker='s', linewidth=2,
         color='#2d6a4f', label='2023')
plt.plot(months, df_monthly['2024'], marker='^', linewidth=2,
         color='#c1440e', label='2024')

plt.title('Madinah — Monthly Umrah Visitors Peak Analysis 2022-2024', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Visitors')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('charts/chart6_monthly_peak.png', dpi=150)
plt.show()
print("Chart 6 saved!")