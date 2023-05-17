# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
#Leila Mehrabi,17/05/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # File name
objFile=None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow=[]  # A list that reads the ',' splitted data from the txt file
strTask="" #User input for Task
strPriority="" #User input for Priority
helpstrExist=0 #helping variable which helps to determine if the added task already exists?
helpstrFound = 0 #helping variable that helps determoine if the entered task exists?



# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.replace("\n","").split(",")#replace the new line character and then splits each row by , character
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}#saves the row as a dictionory
    lstTable.append(dicRow)#append the dic row to a table (list)
objFile.close()



# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("   TASK   "+"|"+"  PRIORITY  ")
        print("-------------------------------")
        for row in lstTable:#reads all rows in the list and displays the value
            print(row["Task"]+" | "+row["Priority"])
        input("Press any key to go back to the main menu ")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask=str(input("Please input the task name: "))
        helpstrExist=0 #helping variable which helps to determine if the added task already exists?
        for row in lstTable:#checks to see if the task already exists. If so, it doesn't let the user enter the task
            if(row["Task"].lower()==strTask.lower()):
                print("The task already exists")
                helpstrExist = 1
                break
        #End For
        if(helpstrExist!=1):#if the task doesn't already exist it goes to next step and asks for the priority and adds it to the table
            strPriority=str(input("Please input the task's priority: "))
            dicRow={"Task":strTask,"Priority":strPriority}
            lstTable.append(dicRow)
            continue
        else:
            input("Press any key to continue ")
            continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask=str(input("Please enter the task you want to delete: "))
        helpstrFound = 0 #helping variable that helps determoine if the entered task exists?
        for row in lstTable:
            if(row["Task"].lower()==strTask.lower()):#if the task exists, it deletes the relevant row from the table and informs the user
                lstTable.remove(row)
                print("The task"+" '"+strTask+"' "+"deleted\n")
                input("Press any key to continue ")
                helpstrFound=1
                break
        #End For
        if(helpstrFound!=1):#if the task doesn't exist, it informs the user and goes back to main menu
            print("The task doesn't exist!!")
            input("Press any key to go back to the main menu ")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        while (True):
            strSave = str(input("Are you sure you want to save the current data to the file? y or n? "))
            if (strSave.lower() == 'y'):  # saves the current data to the file
                objfile = open("ToDoList.txt", "w")
                for row in lstTable:
                    objfile.write(row["Task"] + "," + row["Priority"]+"\n")#writes current data to the file
                input("Data saved to the file! \n Press any key to continue")
                objfile.close()
                break
            elif (strSave.lower() == 'n'):
                input("Data didn't save to the file \n Press any key to continue ")
                break
            else:
                print("Please enter only 'y' or 'n': ")  # checks if any key other than y or n is entered by the user
        continue
        #End While
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
            strExit=str(input("Are you sure you want to exit? y or n: "))#double checks if the user really wants to exit?
            if(strExit.lower()=="y"):
                print("End of Program")
                break # and Exit the program
            # TODO: Add Code Here
            else:
                print("Please enter any key to go back to the main menu ")
                continue

    else:
        print("Please choose only 1, 2, 3, 4 or 5!")  # check if any key other than 1,2,3,4,5 is entered by the user
    # End IF
#End While/End of Program
