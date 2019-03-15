# How strings work in Python

# Strings are immutable

wizard = "Harry Potter"

# Strings are collections/arrays of chars, and can be iterated
for letter in wizard:
    print(letter)
    
print("%s " % wizard + "starts with the letter %s" % wizard[0])

# -1 is a valid index! - only on Python 3
print("The last letter in {0} is {1}".format(wizard, wizard[-1]))

# Getting 5 characters starting from index zero
# [0:5] or [:5] prints 0, 1, 2, 3, 4 but not 5!
# [6:] prints from index 6 to end of the string
print(wizard[0:5])
print(wizard[6:])

interpolation = "aaa,bbb,ccc,ddd"
print(interpolation[0::4]) # abcd

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) # Prints 0, skips 3 counting from 0 -> 123456789

# Prints La La La Land
print("La " * 2 + "Land")

# Returns True
print("Harry" in wizard)

print(":".join(wizard)) # add a : between every char

# Manipulation Functions

wizards = [wizard, "Hermione Granger", "Ron Weasley"]

harry = wizard[0]
hermione = wizards[1]
ron = wizards[2]

sentence = "Harry, Ron and Hermione go to Hogwarts School of Witchcraft"

for word in wizards:
    print("%s has %d letters in it." % (word, len(word)))
