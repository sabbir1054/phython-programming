def nearly_equal(a,b):
	count=-1
	for letter in a:
		for letter2 in b:
			if letter==letter2:
				count+=1
	strlen=len(a)
	if count+1==strlen:
		print("True")
	else:
		print("False")

	

nearly_equal("perl","pearl")