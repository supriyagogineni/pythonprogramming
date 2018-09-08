x,y = map(int,raw_input().split())
x = x ^ y
y = x ^ y
x = x ^ y
print("  {0}  {1}".format(x, y)),
