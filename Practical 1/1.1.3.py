from datetime import datetime

date1_str = input()
date2_str = input()

date1 = datetime.strptime(date1_str, '%Y-%m-%d')
date2 = datetime.strptime(date2_str, '%Y-%m-%d')

x= date2 - date1
days_diff = x.days

print(days_diff)
