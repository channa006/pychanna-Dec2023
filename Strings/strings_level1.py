#1 - print length of the Strings 

#s= 'Channabasava'
#print(len(s))

#2 - Print the Character at a Specific Index

#s='Pizza'
#n=4
#
#if not s:
#   print('Empty String')
#elif n<len(s):
#    print(s[n])
#else:
#    print('Out of String')

#3.1 - Reverse a String

#s="Hello"
#print(s[::-1])

#3.1 - Reverse a String

#s='Hello'
#reversed_string = ''.join(reversed(s))
#print(reversed_string)

#4 - First and Last Three Characters of a String

#s = "Amazing"
#n=2 
#
#if len(s) == 0 or len(s)<n*2:
#    print("Invalid String")
#else:
#    print(s[:n] + s[len(s)-n:])

#-------------
#5.1 - Remove Characters at Even Indices 

#s = "Wonderful"
#new_s = ""
#
#for i in range(len(s)):
#    if i % 2 != 0:
#        new_s +=s[i]
#
#print(new_s)

#5.2 

#s = "Amazing"
#new_s = ''
#for i in range (1,len(s),2):
#    new_s+=s[i]
#
#print(new_s)


#------------------------------------------------------------------
#6 - Check if a String Only Contains Numbers

#s = '123' 
#print(s.isdecimal())

#------------------------------------------------------------------
#7 - Remove nth Character from a String

#s = 'Wonderful' 
#new_s=''
#n = 8
#
#if not s:
#    print('Empty String')
#else:
#    for i in range(len(s)):
#         if i!= n:
#            new_s += s[i]
#
#print(new_s)

#------------------------------------------------------------------
#8.1 - Replace a Character in a String

#s = 'Hello' 
#
#curr = 'l'
#new='s' 
#new_s=''
#
#for i in range(len(s)):
#    if s[i] != curr:
#        new_s+=s[i]
#    else:
#        new_s+=new
#
#print(new_s)

#8.2 

#s = 'Hello' 
#curr_char = 'l'
#new_char = 's' 
#new_s=''
#
#for char in s :
#    if char != curr_char:
#        new_s+=char
#    else:
#        new_s+=new_char 
#
#print(new_s)

#8.3 

#s = 'Hello' 
#curr_char = 'l'
#new_char='s'
#
#print(s.replace(curr_char,new_char))


#------------------------------------------------------------------




