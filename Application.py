# referencing material:
# https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
# https://www.geeksforgeeks.org/reading-csv-files-in-python/
# https://www.youtube.com/watch?v=Z8UEc9L1y_w
# https://www.w3schools.com/python/ref_keyword_del.asp
# https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python
# https://stackoverflow.com/questions/930397/how-do-i-get-the-last-element-of-a-list
# https://www.geeksforgeeks.org/writing-csv-files-in-python/

# Import the csv module to handle CSV file operations
import csv
# Define global lists to store data for each attribute of student records
id_student = []
name = []
age = []
major = []
department = []
units = []
uni_loan = []


def load_records():
    # open csv file as file in read mode
    with open("students.csv", mode="r") as file:
        # Create a CSV reader object to read data from the file
        csv_file = csv.reader(file)

        # Skip the header row to avoid including column names in data arrays
        next(csv_file, None)

        # Loop through each row (entry) in the CSV file
        for entry in csv_file:
            # Append data from each column of the current row to corresponding lists
            id_student.append(int(entry[0]))
            name.append(entry[1])
            age.append(int(entry[2]))
            major.append(entry[3])
            department.append(entry[4])
            units.append(int(entry[5]))
            uni_loan.append(entry[6])
    print("Records Loaded successfully")


def display_records():
    # Print the header row with column names, using formatted strings to set fixed widths for each column
    print("{0:10s}".format("ID"),
          "{0:15s}".format("Name"),
          "{0:10s}".format("Age"),
          "{0:25s}".format("Major"),
          "{0:20s}".format("Department"),
          "{0:10s}".format("Units"),
          "{0:10s}".format("Uni_Loan"),
          )

    # Loop through each student's data by index
    for i in range(len(id_student)):
        # Print each student's data on the same line, with formatted spacing for alignment
        # The 'end=""' prevents moving to a new line after each print, keeping all data in one row
        print("{0:10d}".format(id_student[i]), end=" ")
        print("{0:15s}".format(name[i]), end=" ")
        print("{0:10d}".format(age[i]), end=" ")
        print("{0:25s}".format(major[i]), end=" ")
        print("{0:20s}".format(department[i]), end=" ")
        print("{0:10d}".format(units[i]), end=" ")
        print("{0:10s}".format(uni_loan[i]))


def add_record():
    # if id_student is not an empty array, set next_id to the last ID of id_student list plus 1
    if id_student:
        next_id = id_student[-1] + 1
    # if id_student is an empty array, assign 1 to next_id
    else:
        next_id = 1

    # Prompt the user to input details for the new student record and store each input
    next_name = input("Name: ")
    next_age = int(input("Age: "))
    next_major = input("Major: ")
    next_department = input("Department: ")
    next_units = int(input("Units: "))
    next_uni_loan = input("Uni Loan: ")

    # Append each piece of the new record to the corresponding list
    id_student.append(next_id)
    name.append(next_name)
    age.append(next_age)
    major.append(next_major)
    department.append(next_department)
    units.append(next_units)
    uni_loan.append(next_uni_loan)
    print("Record added!")


def delete_record():
    # Prompt the user to enter the ID of the record to be deleted
    input_id = int(input("Enter the ID to be deleted: "))

    # Check if the entered ID exists in the id_student list
    if input_id in id_student:
        # find the index of the id to be deleted
        delete_id = id_student.index(input_id)
        # Delete the corresponding entries in all parallel arrays based on the found index
        del id_student[delete_id]
        del name[delete_id]
        del age[delete_id]
        del major[delete_id]
        del department[delete_id]
        del units[delete_id]
        del uni_loan[delete_id]
        print("Record deleted")
    else:
        # Inform the user if the entered ID does not exist
        print("No such ID exists!")


def save_record():
    # Open "students.csv" in write mode, specifying no extra newline characters
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row with column names
        writer.writerow(["ID", "Name", "Age", "Major", "Department", "Units", "Uni Loans"])

        # Loop through each student's data by index and write it to the file
        for i in range(len(id_student)):
            # Write the current student's record as a row in the CSV
            writer.writerow([id_student[i], name[i], age[i], major[i], department[i], units[i], uni_loan[i]])
    print("Records saved successfully")


def menu():
    print("Please choose:")
    print("1. Load records")
    print("2. Display records")
    print("3. Add records")
    print("4. Delete records")
    print("5. Save records")
    print("6. Exit")


# variable to control the while loop
my_menu_loop = True

# create while loop to keep the menu active until the user chooses to exit
while my_menu_loop:
    # Display the menu options to the user
    menu()
    # Prompt the user to choose an option and convert the input to an integer
    numChosen = int(input("Please choose: "))

    # Perform actions based on the user's choice
    if numChosen == 1:
        load_records()
    elif numChosen == 2:
        # Check if there are any records to display
        if id_student:
            print("Display record below:")
            display_records()
        else:
            print("No records found!")
    elif numChosen == 3:
        add_record()
    elif numChosen == 4:
        delete_record()
    elif numChosen == 5:
        save_record()
    else:
        # End the loop and exit if the user chooses option 6 or an invalid option
        my_menu_loop = False
        print("Exiting the menu")
