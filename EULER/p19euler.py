from datetime import datetime as dt
print(sum([1 for x in range(1901,2001) for y in range(1,13)
			 if dt(x,y,1).weekday()==6]))