n=int(input())
x=bin(n)
y=x[2::]




#print(y)

# .split('0') will split the consecutive ones from a zero.
#print(y.split("0"))

# we need the maximum length not the maximum value.
# therefore map will maps the length and max will provide us
# the maximum length.
# Map is used as max won't take 2 parameters.


print(max(map(len,y.split("0"))))   ## Maximum length of consecutive ones.


'''

INPUT: 22

OUTPUT:

10110  (Value of y)= 22 in binary

['1', '11', '']   (Output of y.split)


2   (Final output)

Explanation:
maximum consecutive ones length is 2. 
  
'''
