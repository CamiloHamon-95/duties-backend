from datetime import datetime

my_date = 1716943385

timestamp = datetime.fromtimestamp(my_date)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.now())
print(datetime.timestamp(datetime.now()))
print(int(datetime.timestamp(datetime.now())))