def string_splitter(a_str):
    ind1 = 0
    n_list = []
    while a_str.find(' ',ind1) >= 0:
        ind2 = a_str.find(' ',ind1)
        print(ind2)
        n_list.append(a_str[ind1:ind2])
        ind1 = ind2+1
    n_list.append(a_str[ind1:])
    return n_list

print(string_splitter("Hello world"))    