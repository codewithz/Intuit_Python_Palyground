from datetime import datetime
import time

date1=datetime(2022,4,23)
print(date1)

current_date=datetime.now()
print(current_date)

incoming_date="23/04/2021"

date2=datetime.strptime(incoming_date,"%d/%m/%Y")
print(date2)

date3=datetime.fromtimestamp(time.time())
print(date3)

print("Date:",current_date)
print("Formatted Date",current_date.strftime("%d/%m/%Y"))