# Python program for Break and Continue

print("Example for Break Keyword")

for i in range(1,11):
	if i>5:
		break
	print(i)


print("Example for Conitnue Keyword")

for i in range(1,11):
	if i<5:
		continue
	print(i)


# Python program for Pass keyword

a = 4

if a<5:
	pass
else:
	print("a is greater than 5")
