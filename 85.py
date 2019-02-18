k = raw_input().rstrip()
evens = oddk = ''
for i, j in enumerate(k):
	if i & 1 == 0:
		evens += j
	else:
		oddk += j

print(evens + " " + oddk)
