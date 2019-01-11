mystery_string = "my cat your cat"

#Add some code below that will count and print how many
#times the character sequence "cat" appears in mystery_string.
#For example, for the string above, it would print 2.
#
#This one is tricky! Think carefully about for-each loops,
#conditionals, and booleans. How can you track what character
#you're currently looking for? We expect you'll use a loop
#and a single big conditional, but there are other approaches
#as well. Try to stick with the topics we've covered so far.
count = 0
for i in range(len(mystery_string)+1):
    char = mystery_string[i:i+3]
    #print(char)
    if char == "cat":
        count += 1
print(count)        