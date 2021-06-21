#PF-Exer-18

def find_leap(given):
    list_of_leap_years
    count=0
    while count < 4:
        if (given%4==0) & ((given%100!=0) | (given%400==0)):
            leap=given
            print(leap)
            break
        else:
            given=given+1
            count=count+1

    for x in range(15):
        given_year = given_year + 4
        x = x + 1
        list_of_leap_years.append(given_year)
return
find_leap(2002)




for x in range(15):
               given_year=given_year+4
               x=x+1
               list_of_leap_years.append(given_year)



