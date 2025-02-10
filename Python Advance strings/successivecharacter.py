# Python3 code to demonstrate working of 
# Successive Characters Frequency 
# Using count() + loop + re.findall() 
import re 
	
# initializing string 
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'

# printing original string 
print("The original string is : " + str(test_str)) 

# initializing word 
que_word = "geek"

# Successive Characters Frequency 
# Using count() + loop + re.findall() 
temp = [] 
for sub in re.findall(que_word + '.', test_str): 
	temp.append(sub[-1]) 

res = {que_word : temp.count(que_word) for que_word in temp} 

# printing result 
print("The Characters Frequency is : " + str(res)) 
