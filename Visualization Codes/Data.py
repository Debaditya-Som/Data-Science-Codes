#importing the csv module
import csv

mydict=[{'branch': 'COE','cgpa':'9.0','name':'Debaditya','year':'2'},
        {'branch': 'COE','cgpa':'9.1','name':'Som','year':'2'},
        {'branch': 'CSBS','cgpa':'8.0','name':'Ricky','year':'1'},
        {'branch': 'IT','cgpa':'9.5','name':'Aditya','year':'3'},
        {'branch': 'MCE','cgpa':'7.0','name':'Philips','year':'3'},
        {'branch': 'ECE','cgpa':'9.0','name':'Evan','year':'2'}]


#field names
fields = ['name','branch','year','cgpa']

#name of csv file
filename = "university_record.csv"

#writing to csv
with open(filename,'w') as csvfile:
    #creating csv dict writer object
    writer = csv.DictWriter(csvfile,fieldnames = fields)

    #writing headers(field name)
    writer.writeheader()

    #writing data rows
    writer.writerows(mydict)