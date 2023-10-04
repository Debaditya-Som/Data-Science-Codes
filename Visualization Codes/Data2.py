import csv
filename = "aapl.csv"

fields=[]
rows=[]

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for rows in csvreader:
        rows.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))

print('Field names are:'+','.join(field for field in fields))

print("\nFirst 5 rows are:\n")
for rows in rows[5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')    