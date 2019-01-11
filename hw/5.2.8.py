#Write a function called rabbit_hole. rabbit_hole should have
#two parameters: a dictionary and a string. The string may be
#a key to the dictionary. The value associated with that key,
#in turn, may be another key to the dictionary.
#
#Keep looking up the keys until you reach a key that has no
#associated value. Then, return that key.
#
#For example, imagine if you had the following dictionary.
#This one is sorted to make this example easier to follow:
#
# d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
#      "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
#      "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
#      "rat": "ram", "ram": "rat"}
#
#If we called rabbit_hole(d, "bat"), then our code should...
#
# - Look up "bat", and find "pig"
# - Look up "pig", and find "cat"
# - Look up "cat", and find "dog"
# - Look up "dog", and find "ant"
# - Look up "ant", and find no associated value, and so it would
#   return "ant".
#
#Other possible results are:
#
# rabbit_hole(d, "bat") -> "fly"
# rabbit_hole(d, "ewe") -> "hen"
# rabbit_hole(d, "jay") -> "doe"
# rabbit_hole(d, "yak") -> "yak"
#
#Notice that if the initial string passed in is not a key in
#the dictionary, that string should be returned as the result as
#well.
#
#Note, however, that it is possible to get into a loop. In the
#dictionary above, rabbit_hole(d, "rat") would infinitely go
#around between "rat" and "ram". You should prevent this: if a
#key is ever accessed more than once (meaning a loop has been
#reached), return the boolean False.
#
#Hint: If you try to access a value from a dictionary that does
#not exist, a KeyError will be raised.
def rabbit_hole(a_dict,a_key,old_key=''):
    try:
        if a_dict[a_key] == old_key:
            print(False)
            return False
        return rabbit_hole(a_dict,a_dict[a_key],a_key)
    except KeyError:
        print(a_key)
        return a_key    



#If your function works correctly, this will originally
#print: ant, hen, doe, yak, False, each on their own line.
d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

rabbit_hole(d, "bat")
rabbit_hole(d, "ewe")
rabbit_hole(d, "jay")
rabbit_hole(d, "yak")
rabbit_hole(d, "rat")


