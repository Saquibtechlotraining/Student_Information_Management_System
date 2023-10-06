# Student Management System (Extended Version)

user_id_list = ["saquib@634", "kevin@123", "abhishek@9000", "sania@350"]
place_list = ["london", "capetown", "zurich", "italy"]
course_list = ["datascience", "fullstack", "blockchain", "devops"]
roll_no_list = [121, 561, 1050, 2903]

while True:
    print("<<<<<Students Details>>>>>")

    x = """    1. Add a Student
    2. Delete a Student
    3. Find a Student by User - ID
    4. Find a Student by Roll number
    5. Update Student Details
    6. Show all Student
    7. Exit"""
    print(x)

    ch = int(input("Enter the choice:"))

    if ch == 1:
        user_id = input("Enter the user id of a new student:")
        if user_id not in user_id_list:
            user_id_list.append(user_id)
            place = input("Enter the place of a new student:")
            place_list.append(place)
            course = input("Enter the course of a new student:")
            course_list.append(course)
            roll_number = int(input("Enter the roll number of a new student:"))
            roll_no_list.append(roll_number)
            print(user_id_list)
            print(place_list)
            print(course_list)
            print(roll_no_list)
        else:
            print("Already exist in a list")

    elif ch == 2:
        user_id = input("Enter the user ID of student whose details we want to delete:")
        if user_id in user_id_list:
            student_detail_removed = user_id_list.index(user_id)
            print(user_id_list.pop(student_detail_removed))
            print(place_list.pop(student_detail_removed))
            print(course_list.pop(student_detail_removed))
            print(roll_no_list.pop(student_detail_removed))
        else:
            print("We cannot delete this User id because it doesn't exist in list")


    elif ch == 3:
        user_id = input("Enter the user ID of student of which  we want to find the details:")
        if user_id in user_id_list:
            student_detail = user_id_list.index(user_id)
            print("User ID:", user_id_list[student_detail])
            print("Place:", place_list[student_detail])
            print("Course:", course_list[student_detail])
            print("Roll number:", roll_no_list[student_detail])
        else:
            print("This user id doesn't exist")

    elif ch == 4:
        roll_number = int(input("Enter the roll number:"))
        if roll_number in roll_no_list:
            roll_n = roll_no_list.index(roll_number)
            print("User ID:", user_id_list[roll_n])
            print("Place List:", place_list[roll_n])
            print("Course_list:", course_list[roll_n])

    elif ch == 5:
        print("Which information you want to Update:")
        y = """        1. Place
        2. Course
        3. Roll Number"""
        print(y)

        op = int(input("Choice any one to update the Information of a Student:"))
        if op == 1:
            user_id = input("Enter the Student User Id:")
            if user_id in user_id_list:
                for_index = user_id_list.index(user_id)
                place_update = input("Enter the new Place:")
                place_list[for_index] = place_update
                print("New Updated Place of a Student:", place_list)
            else:
                print("The Student of this User doesn't exist")

        elif op == 2:
            user_id = input("Enter the Student User Id:")
            if user_id in user_id_list:
                for_index = user_id_list.index(user_id)
                course_update = input("Enter the new Course:")
                course_list[for_index] = course_update
                print("New Updated Course of a Student:", course_list)
            else:
                print("The Student of this User doesn't exist")

        elif op == 3:
            user_id = input("Enter the Student User Id:")
            if user_id in user_id_list:
                for_index = user_id_list.index(user_id)
                roll_no_update = int(input("Enter the new Roll Number:"))
                roll_no_list[for_index] = roll_no_update
                print("New Updated Roll Number of a Student:", roll_no_list)
            else:
                print("The Student of this User doesn't exist")

        else:
            print("Invalid Operation")

    elif ch == 6:
        print("...STUDENTS DETAILS...")
        print("User IDS", "|", "Places", "|", "Courses","|","roll_no_list")
        for USER_IDS, PLACES, COURSES, ROLL_NO in zip(user_id_list, place_list, course_list, roll_no_list):
            print(USER_IDS, "|", PLACES, "|",  COURSES, "|", ROLL_NO)

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
