########################################################
# TRAINING
# https://www.youtube.com/watch?v=7utwZYKweho
# 9:41 - Strings
# 17:06 - Math
# 22:55 - Variables and Methods
# 33:16 - Functions
# 42:18 - Boolean Expressions and Relational Operators
# 50:56 - Conditional Statements
# 57:58 - Lists
# 1:10:15 - Tuples
# 1:12:30 - Looping
# 1:17:03 - Advanced Strings
# 1:29:47 - Dictionaries
# COMMENTING
# Hmmm.. Using multi-line strings (or docstrings) for commenting? Not sure yet!
# https://www.w3schools.com/python/python_comments.asp
# w3schools does not really covers the docstrings
# DOCSTRINGS
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
# https://google.github.io/styleguide/pyguide.html
# https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
# See below for some fun exercises & documentation
########################################################


########################################################
print("\n" + "### Strings ###" + "\n")
#let's develop first program
print("Hello, world!")
print("""This string runs
multiple lines!""") #triple quote for multi-line
print("This string is "+"awesome!") #we can also concatenate
#print('\n') #new line
print("Test that new line out")
########################################################
print("\n" + "### Math ###" + "\n")
print(50+50) #add
print(50-50) #substract
print(50*50) #multiply
print(50/50) #divide --> float result
print(50+50-50*50/50) #PEMDAS
print(50**2) #exponents
print(50%6) #modulo - takes what is left over
print(50/6) #divisin with remainder (or a float)
print(50//6) #no remainder
########################################################
print("\n" + "### Variables and Methods ###" + "\n")
quote = "All is fair in love and war."
print(quote)
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case - like a title
print(len(quote)) #counts characters - do not forget space is a character
name = "Burak" #string
age = 36 #int
gpa = 3.7 #float - has a decimal
print(int(age))
print(int(30.1))
print(int(30.9)) #will it round? No.
#print("My name is " + name + " and I am " + age + " years old.") #check line - google the "TypeError:"
print("My name is " + name + " and I am " + str(age) + " years old.")
age += 1
print(age)
birthday = 1
age += birthday
print(age)
########################################################
print("\n" + "### Functions ###" + "\n")
def who_am_i(): #this is a function without parameters
    name = "Burak" #local variable
    age = 46
    print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()
#print(age) - the variable in the function is local
def add_one_hundred(num):
    print(num + 100)
add_one_hundred(100)
def add(x,y):
    print(x + y)
add(7,7)
def multiply(x,y):
    return x * y
print(multiply(7,7))
def square_root(x):
    print(x ** .5)
square_root(64)
def nl(): #let's create our new line function
    return("\n")
########################################################
print(nl() + "### Boolean Expressions and Relational Operators ###" + nl()) #true or false
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
print(bool1,bool2,bool3,bool4)
print(type(bool1))
bool5 = "True"
print(type(bool5))
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7> 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True
test_not = not True #False
#google Python Truth Table
########################################################
print(nl() + "### Conditional Statements ###" + nl()) #if/then/else
def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"
print(drink(3))
print(drink(1))
def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too young and too poor."
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))
########################################################
print(nl() + "### Lists ###" + nl()) #have brackets [] and they have items
movies = ["V for Vendetta", "Law Abiding Citizen", "Batman Begins", "Thor: Ragnarok"]
print(movies[1]) #calling an index #It actually starts with 0 #Returns the second item
print(movies[0]) #returns the first item
print(movies[1:3]) #return the first index number given right until the last number, but not include the last number
print(movies[1:]) #return everything begining of index number given
print(movies[:1]) #return everything up until the index number given
print(movies[-1]) #return last item in list
print(len(movies)) #count items in the list
movies.append("Iron Man") #appends to the end of the list
print(movies)
movies.insert(2, "The Last Samurai") #insert object before index 
print(movies)
movies.pop() #removes the last item
print(movies)
movies.pop(0) #removes the first item
print(movies)
movies2 = ["Avengers: Infinity War", "Avengers: Endgame"]
movies_combined = movies + movies2
print(movies_combined)
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]] #2 dimensional list
bobs_grade = grades[0][1] #Index 0 --> ["Bob, 82"] - Second item --> 82
print(bobs_grade)
grades[0][1] = 83
print(grades)
########################################################
print(nl() + "### Tuples ###" + nl()) #lists do not change and wotk with () #immutable
letter_grades = ("a", "b", "c", "d", "f")
print(letter_grades[1])
#letter_grades.pop --> AttributeError: 'tuple' object has no attribute 'pop'
########################################################
print(nl() + "### Looping ###" + nl())
#for loops - start to finish of an iterate
#ping all the 192.168.1.1-254 - use for loop maybe
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)
#while loops - execute as long as True
i = 1
while i < 10:
    print(i)
    i += 1
########################################################
print(nl() + "### Advanced Strings ###" + nl())
my_name = "Burak" #strings are immutable
print(my_name[0]) #first letter
print(my_name[-1]) #last letter
sentence = "This is a sentence."
print(sentence[:4])
print(sentence.split()) #delimeter - deafult is space
sentence_split = sentence.split() #split the sentence in to words
sentence_join = " ".join(sentence_split) #join them with having space character as delimeter
print(sentence_join)
quote = "He said, 'give me all your money'"
#quote = 'He said, "give me all your money"' #alternative
print(quote)
quote = "He said, \"give me all your money\"" #character escaping
print(quote)
too_much_space = "                                                       hello                  "
print(too_much_space)
print(too_much_space.strip()) #eliminates the space characters
print("A" in "Apple") #returns True
print("a" in "Apple") #returns False - case sensitivity
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #impored way of doing this - Manhattan vs. MaNhaTTan
movie = "V for Vendetta"
print("My favorite movie is " + movie +".")
print("My favorite movie is {}.".format(movie)) #using the String format method
print("My favorite movie is %s." % movie) #percent formatting
print(f"My favorite movie is {movie}.") #f string literal - latest and greatest way of doing it in Python 3
########################################################
print(nl() + "### Dictionaries ###" + nl()) #key/value pairs {}
drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the key, price is the value
print(drinks)
employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees["Legal"] = ["Mr. Frond"] #adds new key/value pair - appends to the end
print(employees)
employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key/value pair as well
print(employees)
drinks["White Russian"] = 8
print(drinks)
print(drinks.get("White Russian"))