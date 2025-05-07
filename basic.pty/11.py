import calendar

date1 = (2014, 7, 2)
date2 = (2015, 9, 13)

diff = abs(date1[0] - date2[0]) * 365 + abs(date1[1] - date2[1]) * 30 + abs(date1[2] - date2[2])
print("Difference between two dates is", diff, "days")