import csv

with open('employee_birthday.csv', mode='w') as csv_file:
    fieldnames = ['name', 'department', 'birthday month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'John Smith', 'department': 'Accounting', 'birthday month': 'November'})
    writer.writerow({'name': 'Erica Meyers', 'department': 'IT', 'birthday month': 'March'})

with open('employee_birthday.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
   