# referencing material:
# https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
# https://www.geeksforgeeks.org/python-convert-string-truth-values-to-boolean/
import csv

id_student = []
name = []
age = []
major = []
department = []
units = []
uni_loan = []

with open("students.csv", mode="r") as file:
    csvFile = csv.reader(file)
    next(csvFile)
    for entry in csvFile:
        id_student.append(entry[0])
        name.append(entry[1])
        age.append(int(entry[2]))
        major.append(entry[3])
        department.append(entry[4])
        units.append(int(entry[5]))
        uni_loan.append(entry[6])


print("{0:10s}".format("ID"),
      "{0:15s}".format("Name"),
      "{0:10s}".format("Age"),
      "{0:25s}".format("Major"),
      "{0:20s}".format("Department"),
      "{0:10s}".format("Units"),
      "{0:10s}".format("Uni_Loan"),
      )

for i in range(len(id_student)):
    print("{0:10s}".format(id_student[i]), end=" ")
    print("{0:15s}".format(name[i]), end=" ")
    print("{0:10d}".format(age[i]), end=" ")
    print("{0:25s}".format(major[i]), end=" ")
    print("{0:20s}".format(department[i]), end=" ")
    print("{0:10d}".format(units[i]), end=" ")
    print("{0:10s}".format(uni_loan[i]))


