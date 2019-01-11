#Write a function called st_dev. st_dev should have one
#parameter, a filename. The file will contain one integer on
#each line. The function should return the population standard
#deviation of those numbers.
#The formula is a bit complex, though, and since this is a
#CS class and not a math class, here are the steps you would
#take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
#HINT: You might find this easier if you load all of the
#numbers into a list before trying to calculate the average.
#Either way, you're going to need to loop over the numbers
#at least twice: once to calculate the mean, once to
#calculate the sum of the differences.


#Add your function here!
def st_dev(filename):
    out = open(filename,'r')
    num_l = out.readlines()
    mean = 0
    sum_diff = 0
    count = 0
    for item in num_l:
        mean += int(item)
        count += 1
    for item in num_l:
        sum_diff += (int(item) - mean/count)**2
    #print(mean)
    #print(count)
    #print(sum_diff)
    result = (sum_diff/count)**(1/2)
    out.close()
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))


