#Practice Day-1

name = 'Fadhli'
location = 'Kuala Lumpur'
target_hour_daily = 2

input_hourly = input('Berapa jam actual lu ngoding hari ini? ')
actual_hourly = float(input_hourly)

total_hour_monthly = actual_hourly * 30

print('\n===============================')
print(f'Developer : {name.upper()}')
print(f'Location : {location.title()}')
print(f'Target : {target_hour_daily} hour/day')
print(f'Actual : {actual_hourly} hour/day')
print(f'projection : {total_hour_monthly:.1f} hour/month')
print('=================================')

