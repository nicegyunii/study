'''
Created on 2018/09/07

@author: user36-pci
'''
#~python # coding=utf-8 ~

import test.import_test

test.import_test.print_name()

import calendar
htmlCalendar = calendar.HTMLCalendar(calendar.SUNDAY)

for i in range(1,13):
    print(i,"月")
    s = htmlCalendar.formatmonth(2018,2)
    print(s)
