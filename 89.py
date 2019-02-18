def isIsogram(k):
	charMap = {}
	for m in k:
		if m in charMap:
			return False
		else:
			charMap[m] = 1
	return True
k = raw_input().rstrip()
print("Yes" if isIsogram(k) else "No")
