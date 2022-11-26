#to print leap years between two given dates as input
#display format as you wish
date_1 = list(map(int,input("Enter starting date in dd-mm-yyyy: ").split("-")))
date_2 = list(map(int,input("Enter ending date in dd-mm-yyyy: ").split("-")))
year_1 = date_1[2]       # taking input from user for starting year
year_2 = date_2[2]       # taking input from user for ending year
leap_yr = []                                             # creating empty lists
year = []                                 
for i in range(year_1,(year_2)+1):                    # loop for starting year to ending year
    if i % 4 == 0:                                 # conditions for checking leap year or not
        if i % 100 != 0:
            leap_yr.append(i)                      # using append function to store value
                                                   # in the list
        elif i % 100 == 0:
            if i % 400 == 0:
                leap_yr.append(i)
            else:
                year.append(i)
    else:
        year.append(i)
print("leap year: ", leap_yr)                                            # printing leap year
print("Non leap year: " , year)                                        # printing non- leap years