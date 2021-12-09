# Amina Haq | Project 6 | Playing around with Python

# Student class
class Student(object):
    # initialize values for studentid, fname, lname, level, and an empty list of courses
    def __init__(self, student_id, lname, fname, level):
        self.studid = student_id
        self.lname = lname
        self.fname = fname
        self.level = level
        self.courses = []

    # function that adds courses to the students list of courses
    def addcourse(self, courselist):
        for course in courselist:
            if len(course) < 1:
                continue
            self.courses.append(course)

    # returns a string of the student's information formatted as described
    def __str__(self):
        classes = ""
        for course in self.courses:
            classes = classes + course + "\n"
        return "UID: " + self.studid + "\n" + "First Name: " + self.fname + "\n" + "Last Name: " + self.lname + "\n" + \
               "Level: " + self.level + "\n" + "CLASSES: " + "\n" + classes + "………………" + "\n" + "………………" + "\n\n"


students = []  # list of students
courses = []  # list of courses

# try to open the file
try:
    fi = open("studentRecordsIn.txt").readlines()
# if not found throw exception
except FileNotFoundError:
    print("Oops: file was not found!")
# if found continue executing the code normally
else:
    # while the input file has a text line repeat the following loop
    for line in fi:
        row = line.split('	')  # for each line in the file, use tab as delimiter and split into a list of entries
        if len(row) < 5:  # if the entries in a line are less than five, skip it
            continue
        for x in range(4, len(row)):  # add last entries to the list of courses
            courses.append(row[x].strip())
        row = row[:4]  # reduce the line to not contain the courses
        # for each of the four entries, assign values to the corresponding variables
        student_id, fname, lname, level = [i.strip() for i in row]
        # create a student object and initialize it with the values read from the file
        student = Student(student_id, lname, fname, level)
        # add the corresponding courses to the student's course list
        student.addcourse(courses)
        # clear the courses list for the next iteration
        courses.clear()
        # add the student to the list of students
        students.append(student)
    # open a file to write the output to
    fo = open("studentRecordsOut.txt", "w")
    # write the heading to the file and console
    fo.write("Student Records" + "\n\n")
    print("Student Records" + "\n")
    # for each student in the students list print their information to the screen, and write to the output file
    for student in students:
        print(student)
        fo.write(student.__str__())
    # close the output file
    fo.close()
