with open("p059_cipher.txt") as f:
	data=[int(x) for x in f.read().split(",")]
	#print(data)

def decrypt(data,key):
	c=0
	new=[]
	for x in data:
		new.append(x^key[c%3])
		c+=1
	return new


# for a in range(97,123):
# 	for b in range(97,123):
# 		for c in range(97,123):
# 			d=decrypt(data,[a,b,c])
# 			print("NEXT",[a,b,c])
# 			print("".join((chr(x) for x in d)))


d=decrypt(data,[101, 120, 112])
print(sum(d))
#print("".join((chr(x) for x in d)))