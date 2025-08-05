# text = "Hello World"
# print(len(text))         # Length: 11
# print(text.lower())      # "hello world"
# print(text.upper())      # "HELLO WORLD"
# print(text.title())      # "Hello World"
# print(text[0])           # First character: "H"
# print(text[-1])          # Last character: "d"

# text = "PythonProgramming"
# print(text[0:6])         # "Python"
# print(text[:6])          # "Python"
# print(text[6:])          # "Programming"
# print(text[::-1])        # Reverse string

'''Reversing a string using a loop'''
# word = "Jeffrey"
# print(reverse_string(word))
# for i in range(len(word)):
#     print(word[-1 - i], end='')  # Print "syaD" in reverse

# l = [3,6,8,9,10]
# print(l.reverse())
# print(l)

# a = [1, 2, 3, 4, 5].reverse()
# print(a)

'''Concatenation of string'''

# str1 = "Hello "
# str2 = "World"
# str3 = str1 + str2  # Concatenate: "HelloWorld"
# for i in range(len(str3)):
#     if i == 9:
#         print("z", end='')
#     print(str3[i], end='')  # Print "HelloWorld" character by character
# #print(str1 + " " + str2)  # Concatenate with space: "Hello World"

'''replacing the last character of a string'''

# str1 = "Hello "
# str2 = "World"
# str3 = str1 + str2  # "Hello World"

# for i in range(len(str3)):
#     if i == 9:
#         print("z", end='')  # replace character at index 9
#     else:
#         print(str3[i], end='')

# '''Enigma machine simulation'''

alphabets = "abcdefghijklmnopqrstuvwxyz"
text = "apple mango"
for i in range(len(text)):
    if text[i] in alphabets:
        index = alphabets.index(text[i])
        new_index = (index + 3) % len(alphabets)  # Shift by 3 positions
        print(alphabets[new_index], end='')  # Print the shifted character
    else:
        print(text[i], end='')  # Print non-alphabet characters unchanged



# '''Regular expessions example'''
#  # it will only print 10 digits

# import re

# ph_num = "9488989200"  # Make it a string

# if re.fullmatch(r"\d{10}", ph_num):
#     print("Valid phone number")
# else:
#     print("Invalid phone number")
# print(ph_num)  # Print the phone number


# # re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "user@example.com")



# gmail = "jeffrey@Amadisglobal.com"  # Make it a string

# if re.fullmatch(r"[\w_.+-]+@[\w\d]{11}\.[a-zA-Z]+", gmail):
#     print("Valid gmail address")
# else:
#     print("Invalid gmail address")
# print(gmail)  # Print the phone number


# a = [5,6,7,8,9,10]

# for i in range(0,len(a)):
#     print(a[-1 -i]*2,end = ' ')
    
   

