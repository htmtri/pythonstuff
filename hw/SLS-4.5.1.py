#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:

#marta_file = open('../resource/lib/public/marta_01-18-2016.csv', 'r')
marta_file = open('marta_samp.csv','r')
#Prep data in dict form: {station id: tap}
st_data = {}
for lines in marta_file:
    linessplit = lines.split(',')
    if not linessplit[3] in st_data:
        st_data[linessplit[3]] = 0
    st_data[linessplit[3]] += 1

#prep tap list and calculate avg tap
tot_tap = 0
num_st = 0
tap_l = []
for (items,val) in st_data.items():
    num_st += 1
    tot_tap += val
    tap_l.append(val)
avg_tap = tot_tap/num_st
print('Average tap is:',avg_tap) 

#Find closest to avg tap
tap_l.sort()
tap_closest = min(tap_l, key=lambda x:abs(x-avg_tap))
closest_id = []
for items in st_data:
    if st_data[items] == tap_closest:
        closest_id.append(items)
print('Station with closest to avg traffic:',closest_id)

#Find least tap
least_tap = tap_l[0]
least_id = []
for items in st_data:
    if st_data[items] == least_tap:
        least_id.append(items)
print('Station with least traffic:',least_id)        


         
    
