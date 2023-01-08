while(True):
    print("Students : Press 1")
    print("Course : Press 2")
    print("Batch : Press 3")
    print("Department : Press 4")
    print("Examination : Press 5")
    print("Stop : Press 0")
    x = int(input("Enter your choice: "))
    if(x == 0):
        break
    elif(x == 1):
        from student import *
        while(True):
            print("Press 1 to create students")
            print("Press 2 to update students")
            print("Press 3 to remove students")
            print("Press 4 to Create report card of student")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                createStudent(student_id, student_name)
            elif(y == 2):
                ostudent_id = input("Enter old student ID: ")
                updateStudent(ostudent_id)
            elif(y == 3):
                student_id = input("Enter student ID: ")
                removeStudent(student_id)
            elif(y == 4):
                student_id = input("Enter student ID: ")
                reportCard(student_id)
            else:
                print("Invalid input. Try again.")  
    elif(x == 2):
        from course import *
        while(True):
            print("Press 1 to create a course")
            print("Press 2 to view performance of students on course")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                createCourse(course_id, course_name)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                checkPerformance(course_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 3):
        from batch import *
        while(True):
            print("Press 1 to create a batch")
            print("Press 2 to view all students in a batch")
            print("Press 3 to show all courses in a batch")
            print("Press 4 to view performance of all students in a batch")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                batch_name = input("Enter batch name: ")
                createBatch(batch_name)
            elif(y == 2):
                batch_id = input("Enter batch ID: ")
                viewStudents(batch_id)
            elif(y == 3):
                batch_id = input("Enter batch ID: ")
                viewCourses(batch_id)
            elif(y == 4):
                batch_id = input("Enter batch ID: ")
                viewPerformance(batch_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 4):
        from department import *
        while(True):
            print("Press 1 to create a department")
            print("Press 2 to view all betches in a department")
            print("Press 3 to view average performance of all betches in a department")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                department_id = input("Enter department ID: ")
                department_name = input("Enter department name: ")
                createDepartment(department_id, department_name)
            elif(y == 2):
                department_id = input("Enter department ID: ")
                viewBatches(department_id)
            elif(y == 3):
                department_id = input("Enter department ID: ")
                viewPerformanceD(department_id)
            else:
                print("Invalid input. Try again.")
    elif(x == 5):
        from examination import *
        while(True):
            print("Press 1 to enter marks of all students for an exam")
            print("Press 2 to view performance of all students in an exam")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                course_id = input("Enter course ID: ")
                enterMarks(course_id)
            elif(y == 2):
                course_id = input("Enter course ID: ")
                viewPerformanceE(course_id)
            else:
                print("Invalid input. Try again.")
    else:
        print("Invalid input. Try again.")
