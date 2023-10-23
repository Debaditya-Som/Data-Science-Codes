import json
import csv

## specify file paths , along with extension
input_json_file='input.json'
csv_file = 'output.csv'
# Load JSON data from a file
with open(input_json_file) as json_file:
    data = json.load(json_file)
# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as csvfile:
    # Create a CSV writer, write the header row and data rows
    writer = csv.writer(csvfile)
    writer.writerow(data[0].keys())
    for item in data:
        writer.writerow(item.values())
print("Conversion successfull. The output file is saved as : "+ csv_file)

# why is this useful? Usually ML models are trained on CSV files but maybe your data is taken from MongoDB, that stores data in JSON like format.
# this script comes in handy