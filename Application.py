# referencing material:
# https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
# https://www.geeksforgeeks.org/python-convert-string-truth-values-to-boolean/
# https://www.youtube.com/watch?v=Z8UEc9L1y_w
# https://www.w3schools.com/python/ref_keyword_del.asp
import csv
#define global array
id_student = []
name = []
age = []
major = []
department = []
units = []
uni_loan = []


def load_records():
    with open("students.csv", mode="r") as file: #open csv file as file
        csvFile = csv.reader(file) #read the file and store it into csvFile
        next(csvFile) #skip header when reading the file
        for entry in csvFile: #for each row in csvFile
            id_student.append(entry[0]) #append 1st element(index[0]) of each row to id_student array
            name.append(entry[1])
            age.append(int(entry[2]))
            major.append(entry[3])
            department.append(entry[4])
            units.append(int(entry[5]))
            uni_loan.append(entry[6])


def display_records():
    #print header
    print("{0:10s}".format("ID"),
          "{0:15s}".format("Name"),
          "{0:10s}".format("Age"),
          "{0:25s}".format("Major"),
          "{0:20s}".format("Department"),
          "{0:10s}".format("Units"),
          "{0:10s}".format("Uni_Loan"),
          )

    for i in range(len(id_student)): #loop i in index[0]-index[11]
        #print in one line for each student
        print("{0:10s}".format(id_student[i]), end=" ")
        print("{0:15s}".format(name[i]), end=" ")
        print("{0:10d}".format(age[i]), end=" ")
        print("{0:25s}".format(major[i]), end=" ")
        print("{0:20s}".format(department[i]), end=" ")
        print("{0:10d}".format(units[i]), end=" ")
        print("{0:10s}".format(uni_loan[i]))


def add_record():
    pass


def delete_record():
    # load_records()
    input_id = input("Enter the ID to be deleted: ")
    if input_id in id_student:
        delete_id = id_student.index(input_id) #find the index of the id
        del id_student[delete_id] #delete the index id in parallel arrays
        del name[delete_id]
        del age[delete_id]
        del major[delete_id]
        del department[delete_id]
        del units[delete_id]
        del uni_loan[delete_id]
        print("Record deleted")
    else:
        print("No such ID exists!")


def save_record():
    pass


def menu():
    print("Please choose:")
    print("1. Load records")
    print("2. Display records")
    print("3. Add records")
    print("4. Delete records")
    print("5. Save records")
    print("6. Exit")


#variable to control the while loop
my_menu_loop = True
#create while loop
while my_menu_loop:
    menu()
    numChosen = int(input("Please choose: "))
    if numChosen == 1:
        print("Records loaded")
        load_records()
    elif numChosen == 2:
        if id_student:
            print("Display record below:")
            display_records()
        else:
            print("No records found!")
    elif numChosen == 3:
        add_record()
        print("Records added")
    elif numChosen == 4:
        delete_record()
    elif numChosen == 5:
        save_record()
        print("Records saved")
    else:
        my_menu_loop=False #end the loop and exit
        print("Exiting the menu")
