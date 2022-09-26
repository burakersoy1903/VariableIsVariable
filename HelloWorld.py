########################################################
#TRAINING
#https://www.youtube.com/watch?v=7utwZYKweho
#9:41 - Strings
#17:06 - Math
#22:55 - Variables and Methods
#COMMENTING
#Hmmm.. Using multi-line strings (or docstrings) for commenting? Not sure yet!
#https://www.w3schools.com/python/python_comments.asp
#w3schools does not really covers the docstrings
#DOCSTRINGS
#https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
#https://google.github.io/styleguide/pyguide.html
#https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
########################################################

print('\n')
#STRINGS
#Comments
#Let's develop first program
print("Hello, world!")
print("""This string runs
multiple lines!""") #triple quote for multi-line
print("This string is "+"awesome!") #We can also concatenate
#print('\n') #new line
print("Test that new line out")

print('\n')
#MATH
print(50+50) #add
print(50-50) #substract
print(50*50) #multiply
print(50/50) #divide --> float result
print(50+50-50*50/50) #PEMDAS
print(50**2) #exponents
print(50%6) #modulo - takes what is left over
print(50/6) #divisin with remainder (or a float)
print(50//6) #no remainder

print('\n')
#VARIABLES AND METHODS
quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case --Like a title
print(len(quote)) #counts characters #Do not forget space is a character
name = "Burak" #string
age = 36 #int
gpa = 3.7 #float #has a decimal
print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No.
#print("My name is " + name + " and I am " + age + " years old.") #Check line #Google the "TypeError:"
print("My name is " + name + " and I am " + str(age) + " years old.")
age += 1
print(age)
birthday = 1
age += birthday
print(age)

print('\n')
#FUNCTIONS
