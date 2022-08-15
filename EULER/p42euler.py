with open("p042_words.txt", "r") as f:
	data=[x[1:-1] for x in f.read().split(",")]

data.sort()
print(data)
letter= {}
for x in range(1, 27):
	letter[chr(x+64)]=x

print(letter)
score=[sum([letter[y] for y in x]) for x in data]
print(score)
nmax=max(score)
triangles=[]
for n in range(nmax+1):
	triangles.append(0.5*n*(n+1))
found=0
for x in score:
	if x in triangles:
		found+=1

print(found)