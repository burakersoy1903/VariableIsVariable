########################################################
# This is why we are here
# https://cryptopals.com/sets/1/challenges/2

# Well let's learn before we implement
# https://www.youtube.com/c/nccgroup/videos
# https://youtu.be/PeCTdtgRhVg

# Further reading:
# https://docs.python.org/3/library/functions.html#zip
# https://www.w3schools.com/python/ref_func_zip.asp#:~:text=The%20zip()%20function%20returns,iterator%20are%20paired%20together%20etc.
# https://docs.python.org/3/library/timeit.html
# https://www.geeksforgeeks.org/timeit-python-examples/

# See below for some fun exercises & documentation
########################################################

a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
b = bytes.fromhex("686974207468652062756c6c277320657965")


########################################################
###Ordinals
###https://medium.com/codex/python-ord-getting-the-ordinal-value-of-a-unicode-character-57513b061105#:~:text=The%20term%20ordinal%20means%20countable,encoded%20representations%2C%20or%20sheer%20hobbyism.
###The term ordinal means countable and in the context of Python's ord function will return the integer value assigned to a character in the Unicode encoding system. 
###This can be useful when converting between bytes to strings, binary to encoded representations, or sheer hobbyism.
for ch in b'abc':
    print(ch)
print(ord('a'))
########################################################

########################################################
###Let's benchmark different methods
#import timeit
#code snippet to be executed only once
#mysetup = ""
#code snippet whose execution time is to be measured
#mycode = '''
#def iter_1(a,b):
#    for i in range(min(len(a), len(b))):
#        a[i], b[i]
#'''
#timeit statement
#print (timeit.timeit(setup = mysetup,
#                     stmt = mycode,
#                     number = 10000)) #the execution time(in seconds) for 10000 iterations of the code snippet
#code snippet whose execution time is to be measured
#mycode = '''
#def iter_2(a,b):
#    for byte_1, byte_2 in zip(a,b):
#        byte_1, byte_2
#'''
#timeit statement
#print (timeit.timeit(setup = mysetup,
#                     stmt = mycode,
#                     number = 10000)) #the execution time(in seconds) for 10000 iterations of the code snippet
########################################################