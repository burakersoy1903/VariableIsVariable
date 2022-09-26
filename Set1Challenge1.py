########################################################
#This is why we are here
#https://cryptopals.com/sets/1/challenges/1

# Well let's learn before we implement
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# Article --> "The ASCII values of the characters P, y, t, h, o, n are 15, 50, 45, 33, 40, 39 respectively"
# The truth --> "The ASCII values of the characters P, y, t, h, o, n are 80, 121, 116, 104, 111, 110 respectively"

# Well let's learn before we implement
# https://youtu.be/Yg1ZWegeZiM

#See below for some fun exercises & documentation
########################################################

from base64 import b16decode, b64encode 
data_hex = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
data_raw = b16decode(data_hex, casefold=True)
data_b64 = b64encode(data_raw)
print(data_b64)

########################################################
###Exploring b16decode
#from base64 import b16decode

#data_hex = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
##print(b16decode(data_hex)) #binascii.Error: Non-base16 digit found #Case sensitive #Only uppercase
##print(b16decode(data_hex.upper())) #one solution
##help(b16decode) #Optional casefold is a flag specifying whether a lowercase alphabet is acceptable as input.  For security purposes, the default is False.

#print(b16decode(data_hex, casefold=True)) #other solution #ignores the case sensitivity
########################################################


########################################################
###Exploring encoding to ASCII directly #In progress #Continue testing encoding and decoding
#import base64

#message = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
##message_bytes = message.encode('ascii')
#base64_bytes = base64.b64encode(message)
#print(base64_bytes)
#base64_message = base64_bytes.decode('ascii')

#print(base64_message)
########################################################


########################################################
###Exploring options for hex-decoding in an interpreter
#data_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#print(type(data_hex))
#print(bytes.fromhex(data_hex))
########################################################