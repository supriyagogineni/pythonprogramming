k = raw_input().rstrip()
digits = []
for m in k:
	if m.isdigit():
		digits.append(m)
print("".join(digits))
