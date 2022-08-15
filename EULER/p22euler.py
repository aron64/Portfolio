with open("p022_names.txt", "r") as f:
	data=[x[1:-1] for x in f.read().split(",")]

data.sort()
print(data)
letter= {}
for x in range(1, 27):
	letter[chr(x+64)]=x

print(letter)
score=[sum([letter[y] for y in x])*(data.index(x)+1) for x in data]

print(sum(score))