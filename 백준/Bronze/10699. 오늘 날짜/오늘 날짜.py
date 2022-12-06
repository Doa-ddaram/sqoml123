import datetime
a = datetime.datetime.now()
if a.hour < 15:
  print(a.strftime('%Y-%m-%d'))
else:
  print(a.strftime('%Y-%m-(%d+1)'))