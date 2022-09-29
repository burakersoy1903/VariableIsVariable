########################################################
#This is why we are here
#https://cryptopals.com/sets/1/challenges/1

# Well let's learn before we implement
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
# Article --> "The ASCII values of the characters P, y, t, h, o, n are 15, 50, 45, 33, 40, 39 respectively"
# The truth --> "The ASCII values of the characters P, y, t, h, o, n are 80, 121, 116, 104, 111, 110 respectively"

# Well let's learn before we implement
# https://youtu.be/Yg1ZWegeZiM

#https://docs.python.org/3/library/base64.html

#Research RFC 4648

#See below for some fun exercises & documentation
########################################################

#You'll need to use this code for the rest of the exercises. Encapsulate it, baby, into a function that we could reuse
from base64 import b16decode, b64encode 
def hex_to_b64(data_hex: bytes) -> bytes: #Type signatures to remind that we're working with bytes and not strings
    return b64encode(b16decode(data_hex, casefold=True))

#If we were to import the script, it will run all of this including the logic and print statements
#Logic incur unnecessary compute and print statements would pollute standard out
#It would be very confusing to whoever's importing this
#Imported and run in main vs. running the Set1Challenge1.py seperately
if __name__ == "__main__":
    data_hex = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    data_b64 = hex_to_b64(data_hex)

    print(f"{data_hex = }")
    print(f"{data_b64 = }")
    
    #Let's check if our result is correct from challenge 1
    if data_b64 == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
        print("It worked!")
    else:
        exit("Conversion failed (this should never happen!")


########################################################
###Conversion Done
#from base64 import b16decode, b64encode 
#data_hex = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" #byte literal
#data_raw = b16decode(data_hex, casefold=True) #Solved the case sensitive nature of b16decode
#data_b64 = b64encode(data_raw)
#print(f"{data_hex = }") #pretty printing
#print(f"{data_raw = }")
#print(f"{data_b64 = }")
########################################################


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
###Exploring options for hex-decoding in an interpreter
#data_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#print(type(data_hex))
#print(bytes.fromhex(data_hex))
########################################################