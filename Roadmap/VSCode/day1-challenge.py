#Challenge day1

name = input('nama lu: ')
weight = float(input('berat lu: '))
protein_per_kg = float(input('kebutuhan gram protein lu: '))

total_protein_daily = weight * protein_per_kg
total_protein_weekly = total_protein_daily * 7



print('\n===================================')
print(f'Developer :{name.upper()}')
print(f'Weight : {weight:.1f}')
print(f'Daily : {total_protein_daily:.1f} protein')
print(f'Weekly : {total_protein_weekly:.1f} protein')
print('=====================================')


