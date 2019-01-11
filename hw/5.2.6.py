#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.

def are_anagrams(str1,str2):
    str1 = (str1.replace(' ','')).lower()
    str2 = (str2.replace(' ','')).lower()
    list1 = list(str1)
    list2 = list(str2)
    if not(len(list1) == len(list2)):
        return False
    else:
        for items in list1:
            if not(items in list2):
                return False
            else:
                list2.remove(items)
        return True            

    


#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.
print(are_anagrams("Elvis", "Lives"))
print(are_anagrams("Elvis", "Live Viles"))
print(are_anagrams("Eleven plus two", "Twelve plus one"))
print(are_anagrams("Nine minus seven", "Five minus three"))
print(are_anagrams('Astronomer', 'Moon Starer'))


