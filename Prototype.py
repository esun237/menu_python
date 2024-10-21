# referencing material:
# https://www.geeksforgeeks.org/reading-csv-files-in-python/
# https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
# https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python

#Team: Trisha Yan, Emma Sun

# Import the csv module to handle CSV file operations
import csv

''' 
Define global lists to store data for each attribute of student records
List to store each column of the csv file
These lists are parallel arrays, meaning that the data at index i in each list corresponds to the same student.
'''
# Initialize lists to store data for each attribute of student records
id_student = []
name = []
age = []
major = []
department = []
units = []
uni_loan = []

# Open the "students.csv" file in read mode
with open("students.csv", mode="r") as file:
    # Create a CSV reader object to read data from the file
    csv_file = csv.reader(file)
    # Skip the header row (if any) to prevent adding column names to data lists
    next(csv_file, None)

    # Loop through each row (entry) in the CSV file
    for entry in csv_file:
        id_student.append(entry[0])
        name.append(entry[1])
        age.append(int(entry[2]))
        major.append(entry[3])
        department.append(entry[4])
        units.append(int(entry[5]))
        uni_loan.append(entry[6])

# Print the header for displaying the records, with formatted columns for alignment
print("{0:10s}".format("ID"),
      "{0:15s}".format("Name"),
      "{0:10s}".format("Age"),
      "{0:25s}".format("Major"),
      "{0:20s}".format("Department"),
      "{0:10s}".format("Units"),
      "{0:10s}".format("Uni_Loan"),
      )

# Loop through each student's data by index to print the records
for i in range(len(id_student)):
    # Print each student's data in a formatted line, with fields aligned by column width
    # The 'end=""' prevents moving to a new line after each print, keeping all data in one row
    print("{0:10s}".format(id_student[i]), end=" ")
    print("{0:15s}".format(name[i]), end=" ")
    print("{0:10d}".format(age[i]), end=" ")
    print("{0:25s}".format(major[i]), end=" ")
    print("{0:20s}".format(department[i]), end=" ")
    print("{0:10d}".format(units[i]), end=" ")
    print("{0:10s}".format(uni_loan[i]))  # Move to a new line after each student's full record
