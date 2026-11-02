import csv


def creating_csv():
    """
      Creates a CSV file and stores student names and exam grades.

      Parameters:
      None

      Variables:
      num_students(int): The number of students the instructor wants to enter.
      csvfile(file): The CSV file being created.
      writer(object): Writes records into the CSV file.
      i(int): Keeps track of the number of students being entered.

      Logic:
      1. Prompts the instructor to enter the number of students.
      2. Opens grades.csv in write mode and creates the file if it doesn't exist.
      3. Writes the column headers into the CSV file.
      4. Uses a for loop to collect each student's information.
      5. Writes each student's name and exam grades as a separate record.

      Return:
      None
      """

    num_students = int(input("Enter number of students: "))

    # Opens the grades.csv file in write mode and creates it if it doesn't exist.
    # The newline argument prevents extra blank lines between records.
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Writes the column headers into the first row of the CSV file.
        writer.writerow(['First Name', 'Last Name', 'Exam 1', "Exam 2", "Exam 3"])

        # This for loop repeats based on the number of students entered.
        for i in range(num_students):

            # Prompts the instructor to enter the student's information.
            # The exam grades are converted into integers before being written.
            print(f"Student {i+1}")
            writer.writerow([
                input("Enter First Name: "),
                input("Enter Last Name: "),
                int(input("Enter Exam 1 grade: ")),
                int(input("Enter Exam 2 grade: ")),
                int(input("Enter Exam 3 grade: ")),
            ])

def reading_csv():
    """
    Reads the grades.csv file and displays student information in tabular format.

    Parameters:
    None

    Variables:
    csvfile(file): The CSV file being opened for reading.
    reader(object): Reads the records stored in the CSV file.
    row(list): Stores each record read from the CSV file.

    Logic:
    1. Opens grades.csv in read mode.
    2. Creates a CSV reader to retrieve the records.
    3. Uses a for loop to go through each row in the file.
    4. Uses f-string formatting to align the information into columns.
    5. Displays each student's information in tabular format.

    Return:
    None
    """

    # Opens the grades.csv file in read mode.
    with open('grades.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Reads each record and displays the information in aligned columns.
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

creating_csv()
reading_csv()