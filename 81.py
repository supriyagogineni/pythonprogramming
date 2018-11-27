def do_stuff(input):
	m, n = [int(m) for m in input.split(" ")]
	print(n-m)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
