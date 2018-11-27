num=int(raw_input(""))
digits = []
while num > 0:
    r = num % 10
    if r & 1 != 0:
        digits.append(str(r))
    num=num/10
digits = reversed(digits)
print (" ".join(digits))
