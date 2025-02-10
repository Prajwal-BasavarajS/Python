def findRotations(str1, str2):
	
	# To count left rotations 
	# of string
	x = 0
	
	# To count right rotations
	# of string
	y = 0
	m = str1
	
	while True:
		
		# left rotating the string
		m = m[len(m)-1] + m[:len(m)-1] 
		
		# checking if rotated and 
		# actual string are equal.
		if(m == str2):
			x += 1
			break
			
		else:
			x += 1
			if x > len(str2) :
				break

	while True:
		
		# right rotating the string
		str1 = str1[1:len(str1)]+str1[0] 
		
		# checking if rotated and actual
		# string are equal.
		if(str1 == str2):
			y += 1
			break
			
		else:
			y += 1
			if y > len(str2):
				break
				
	if x < len(str2):
		
		# printing the minimum
		# number of rotations.
		print(min(x,y))
		
	else:
		print("given strings are not of same kind")
		
# Driver code
findRotations('sgeek', 'geeks')
