#Challenge2 Day1

platform = input('nama platform lu? ')
total_sales = float(input('total omzet lu sebulan? '))
commission_rate = float(input('persentase komisi lu? '))
target_months = int(input('berapa bulan target lu? '))

monthly_commission = total_sales * (commission_rate/100)
total_projection_commission = monthly_commission * target_months

print('\n===================================')
print(f'Platform : {platform.upper()}')
print(f'Total Sales : Rp {total_sales:,.1f}')
print(f'Commission Rate : {commission_rate:.1f}%')
print(f'Monthly Earn : Rp {monthly_commission:,.1f}')
print(f'{target_months}-Month Earn : Rp {total_projection_commission:,.1f}')
print('======================================')