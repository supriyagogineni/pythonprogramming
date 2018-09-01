n = int(input(""))
temp = n
rev = 0
while(temp > 0):
    rem = temp % 10
    rev = rev+rem*rem*rem
    temp//=10
if n == rev:
    print "yes"
else:
    print "no"

