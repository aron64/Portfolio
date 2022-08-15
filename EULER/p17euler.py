base={
	1: 3,#len("one"),#
	2: 3,#len("two"),#
	3: 5,#len("three"),#
	4: 4,#len("four"),#
	5: 4,#len("five"),#
	6: 3,#len("six"),#
	7: 5,#len("seven"),#
	8: 5,#len("eight"),#
	9: 4,#len("nine"),#
	20:6,# len("twenty"),#
	30:6,# len("thirty"),#
	40:5,# len("forty"),#
	50:5,# len("fifty"),#
	60:5,# len("sixty"),#
	70:7,# len("seventy"),#
	80:6,# len("eighty"),#
	90:6,# len("ninety"),#
	10:3,#len("ten"),#
	11:6,#len("eleven"),#
	12:6,#len("twelve"),#
	13:8,#len("thirteen"),#
	14:8,#len("fourteen"),#
	15:7,#len("fifteen"),#
	16:7,#len("sixteen"),#
	17:9,#len("seventeen"),#
	18:8,#len("eighteen"),#
	19:8#len("nineteen"),#
}
letters=0
for x in range(1,1000):#(1,1000):
	hundreds=x//100
	c=0
	if hundreds>0:
		c+=base[hundreds]+7
	tenths=x-hundreds*100
	if tenths!=0:
		if hundreds: c+=3
		if tenths in base:
			c+=base[tenths]
		else:
			at=tenths//10
			c+=base[at*10]+base[tenths-at*10]
	letters+=c
	print(x, c) 
	#print(hundreds, tenths)

letters+=11
print(letters)