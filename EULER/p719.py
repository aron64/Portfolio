
def S(string, n,target):
    if n>target:
        return False
    if len(string)==0:
        if n==target:
        	return True
        else:
        	return None
    if target-n>int(string):
        return None
    c=0
    while(c<len(string)):
        c+=1
        t=S(string[c:],n+int(string[:c]),target)
        if t==False:
        	return None
        elif t:
            return True

print(sum([x*x for x in range(2,10**6+1) if x%9<2 and S(str(x*x),0,x)]))

