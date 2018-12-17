num=int(raw_input())
def calcProduct(num):
	if(len(str(num)) == 1):
		return num
	else:
		return (num%10 * calcProduct(num/10))
print(calcProduct(2143))
