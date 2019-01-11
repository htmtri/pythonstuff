def sort_films(src,des):
    f_in = open(src,'r')
    n_list = []
    for lines in f_in:
        temp = lines.strip().split("\t")
        n_list.append(temp)
    sort_l = sorted(n_list,key=lambda sales: int(sales[1]))
    sort_l.reverse()
    f_out = open(des,'w')
    n_list = []
    for item in sort_l:
        n_list.append('\t'.join(item))
    f_out.write('\n'.join(n_list))    
    f_in.close()
    f_out.close()