#Write a function called alter_list. alter_list should have
#two parameters: a list of strings and a list of integers.
#
#The list of integers will represent indices for the list of
#strings. alter_list should alter the capitalization of all
#the words at the designated indices. If the word was all
#capitals, it should become all lower case. If it was all
#lower case, it should become all capitals. You may assume
#that the words will already be all-caps or all-lower case.
#
#For example:
#
# string_list = ["hello", "WORLD", "HOW", "are", "you"]
# index_list = [0, 2]
# alter_list(string_list, index_list) -> 
#                ["HELLO", "WORLD", "how", "are", "you"]
#
#After calling alter_list, the strings at indices 0 and 2
#have switched their capitalization. 
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#text at that index twice. For example:
#
# string_list = ["hello", "WORLD", "HOW", "are", "you"]
# index_list = [0, 2, 2]
# alter_list(string_list, index_list) -> 
#                ["HELLO", "WORLD", "HOW", "are", "you"]
#
#2 is in index_list twice, so the string at index 2 is
#switched twice: capitals to lower case, then back to
#capitals.
def alter_list(str_l,ind_l):
    for i in ind_l:
        if str_l[i].islower():
            new_str = str_l[i].upper()
            str_l.pop(i)
            str_l.insert(i,new_str)
        elif str_l[i].isupper():
            new_str = str_l[i].lower()
            str_l.pop(i)
            str_l.insert(i,new_str)
    return str_l        

#If your function works correctly, this will originally
#print:
#["hello", "WORLD", "HOW", "are", "you"]
#["HELLO", "WORLD", "HOW", "are", "you"]
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2]))
print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2]))