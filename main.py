#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("welcome to quiz system :)")
print("***********************")

print("choose 1 for professor or 2 for student")
print("***********************")

choice = int(input("enter choice : "))
if choice == 1:
    print("welcome to professor mode")
    print("***********************")
    print("If you want to register your information enter 1")
    print("If you want to login enter 2 ")

    professor_choice = int(input("enter your choice"))
    if professor_choice == 1:
        IDExistence = False
        while not IDExistence:

            id = input("enter your id")
            name = input("enter your name")
            email = input("enter your email")
            password = input("enter your password")
            with open('Professor.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    professor_info=line.split("\\")
                    if professor_info[0] == id:
                        print('ID already exists')
                        IDExistence = True
                        break

            if not IDExistence:
                with open("Professor.txt", "a") as f:
                    f.write(id + "\\" + name + "\\" + email + "\\" + password+"\n")
                print("registered succesfully")
                break
        print("If you want to add new quiz enter 1 ")
        print("If you want to remove quiz enter 2 ")
        print("If you want to list registered students on the system enter 3 ")
        quiz_choice = int(input("enter your choice "))
        if quiz_choice == 1:
            quiz_id = input("Enter quiz id : ")
            quiz_title = input("Enter quiz title : ")
            print("Enter quiz questions")
            exit_option = False
            questions_ids = []
            while not exit_option:
                question_id = input("Enter question id : ")
                question_content = input("Enter question : ")
                print("Enter question choices : ")
                choice_a = input("a) ")
                choice_b = input("b) ")
                choice_c = input("c) ")
                solution=input("Enter the solution : (a/b/c) ")
                questions_ids.append(question_id)
                list_of_answers = choice_a + "," + choice_b + "," + choice_c
                with open("Question.txt", "a") as f:
                    f.write(question_id + "\\" + question_content + "\\" + list_of_answers+"\\"+solution+"\n")
                exit_choice = input("Do you want to finish ? (y/n) ")
                if (exit_choice == 'y'):
                    exit_option = True
                else:
                    exit_option = False
            questions_ids_string = ','.join(questions_ids)
            with open("Quiz.txt", "a") as f:
                f.write(quiz_id + "\\" + quiz_title + "\\" + questions_ids_string+"\n")


        elif quiz_choice==2:
            quiz_id=input("Enter quiz id to remove : ")
            with open('Quiz.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    quiz_info=line.split("\\")
                    if(quiz_id==quiz_info[0]):
                        questions_ids=quiz_info[2]
                        questions_ids_list=questions_ids.split(",")
                        with open('Question.txt', 'r') as fp:
                            lines = fp.readlines()
                        with open("Question.txt", "w") as f:
                            for line in lines:
                                question_info=line.split("\\")
                                if question_info[0] not in questions_ids_list:
                                    f.write(line)
                    with open('Quiz.txt', 'r') as fp:
                        lines = fp.readlines()
                    with open("Quiz.txt", "w") as f:
                        for line in lines:
                            quiz_info = line.split("\\")
                            if quiz_id != quiz_info[0]:
                                f.write(line)

        elif quiz_choice==3:
            with open('Student.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line=line.replace("\n","")
                    student_info=line.split("\\")
                    print("student id : ",student_info[0])
                    print("student name : ", student_info[1])
                    print("student email : ", student_info[2])
                    print("student level : ", student_info[4])
                    print("student age : ", student_info[5])
                    print("\n")
        else:
            print("Please enter a valid choice!")
    elif professor_choice == 2:
        EmailExistence = False
        PasswordExistence = False
        while not EmailExistence and not PasswordExistence:
            EmailExistence = False
            PasswordExistence = False
            email = input("enter your email ")
            password = input("enter your password ")

            with open('Professor.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line=line.replace("\n","")
                    professor_info = line.split("\\")
                    if professor_info[2] == email:
                        EmailExistence = True
                        if professor_info[3] == password:
                            PasswordExistence = True
                            break
                        else:
                            PasswordExistence = False
                            break

            if (EmailExistence == True) and (PasswordExistence == True):
                print("Logged in successfully")
                print("If you want to add new quiz enter 1 ")
                print("If you want to remove quiz enter 2 ")
                print("If you want to list registered students on the system enter 3 ")
                quiz_choice = int(input("enter your choice "))
                if quiz_choice == 1:
                    quiz_id = input("Enter quiz id : ")
                    quiz_title = input("Enter quiz title : ")
                    print("Enter quiz questions")
                    exit_option = False
                    questions_ids = []
                    while not exit_option:
                        question_id = input("Enter question id : ")
                        question_content = input("Enter question : ")
                        print("Enter question choices : ")
                        choice_a = input("a) ")
                        choice_b = input("b) ")
                        choice_c = input("c) ")
                        solution = input("Enter the solution : (a/b/c) ")
                        questions_ids.append(question_id)
                        list_of_answers = choice_a + "," + choice_b + "," + choice_c
                        with open("Question.txt", "a") as f:
                            f.write(question_id + "\\" + question_content + "\\" + list_of_answers+"\\"+solution+"\n")
                        exit_choice = input("Do you want to finish ? (y/n) ")
                        if (exit_choice == 'y'):
                            exit_option = True
                        else:
                            exit_option = False
                    questions_ids_string = ','.join(questions_ids)
                    with open("Quiz.txt", "a") as f:
                        f.write(quiz_id + "\\" + quiz_title + "\\" + questions_ids_string + "\n")


                elif quiz_choice==2:
                    quiz_id = input("Enter quiz id to remove : ")
                    with open('Quiz.txt', 'r') as fp:
                        lines = fp.readlines()
                        for line in lines:
                            line = line.replace("\n", "")
                            quiz_info = line.split("\\")
                            if (quiz_id == quiz_info[0]):
                                questions_ids = quiz_info[2]
                                questions_ids_list = questions_ids.split(",")
                                with open('Question.txt', 'r') as fp:
                                    lines = fp.readlines()
                                with open("Question.txt", "w") as f:
                                    for line in lines:
                                        question_info = line.split("\\")
                                        if question_info[0] not in questions_ids_list:
                                            f.write(line)
                            with open('Quiz.txt', 'r') as fp:
                                lines = fp.readlines()
                            with open("Quiz.txt", "w") as f:
                                for line in lines:
                                    quiz_info = line.split("\\")
                                    if quiz_id != quiz_info[0]:
                                        f.write(line)

                elif quiz_choice == 3:
                    with open('Student.txt', 'r') as fp:
                        lines = fp.readlines()
                        for line in lines:
                            line = line.replace("\n", "")
                            student_info = line.split("\\")
                            print("student id : ", student_info[0])
                            print("student name : ", student_info[1])
                            print("student email : ", student_info[2])
                            print("student level : ", student_info[4])
                            print("student age : ", student_info[5])
                            print("\n")
                else:
                    print("Please enter a valid choice!")

                break
            elif EmailExistence == False:
                print("Email doesn't exist")
            else:
                print("Password is not correct")


    else:
        print("Please enter a valid option")


elif choice == 2:
    print("welcome to student mode")
    print("***********************")
    print("If you want to register your information enter 1")
    print("If you want to login enter 2 ")

    student_choice = int(input("enter your choice"))
    if student_choice == 1:
        IDExistence = False
        while not IDExistence:

            id = input("enter your id")
            name = input("enter your name")
            email = input("enter your email")
            password = input("enter your password")
            level = input("enter your level")
            age = input("enter your age")
            with open('Student.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    student_info = line.split("\\")
                    if student_info[0] == id:
                        print('ID already exists')
                        IDExistence = True
                        break

            if not IDExistence:
                with open("Student.txt", "a") as f:
                    f.write(id + "\\" + name + "\\" + email + "\\" + password + "\\" + level + "\\" + age+"\n")
                print("registered succesfully")
                break
    elif student_choice == 2:
        EmailExistence = False
        PasswordExistence = False
        while not EmailExistence and not PasswordExistence:
            EmailExistence = False
            PasswordExistence = False
            email = input("enter your email ")
            password = input("enter your password ")
            
            with open('Student.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    student_info = line.split("\\")
                    if student_info[2] == email:
                        EmailExistence = True
                        if student_info[3] == password:
                            PasswordExistence = True
                            break
                        else:
                            PasswordExistence = False
                            break
            if (EmailExistence == True) and (PasswordExistence == True):
                print("Logged in successfully")
                exit=False
                while not exit:
                    print("If you want to see all possible quizzes enter 1 ")
                    print("If you want to search for a quiz by title enter 2 ")
                    print("If you want to send quiz answers enter 3 ")
                    choice=int(input("Please enter your choice : "))
                    if (choice==1):
                        print("All Possible Quizzes\n")
                        with open('Quiz.txt', 'r') as fp:
                            lines = fp.readlines()
                            for line in lines:
                                line = line.replace("\n", "")
                                quiz_info = line.split("\\")
                                print("quiz id : ", quiz_info[0])
                                print("quiz title : ", quiz_info[1])
                                print("\n")
                    elif (choice==2):
                        quiz_title=input("enter quiz title : ")
                        with open('Quiz.txt', 'r') as fp:
                            lines = fp.readlines()
                            for line in lines:
                                if quiz_title in line:
                                    line = line.replace("\n", "")
                                    quiz_info = line.split("\\")
                                    print("quiz id : ", quiz_info[0])
                                    print("quiz title : ", quiz_info[1])
                                    print("\n")
                                
                    elif (choice==3):
                        quiz_id=input("Enter quiz id")
                        with open('Quiz.txt', 'r') as fp:
                            lines = fp.readlines()
                            for line in lines:
                                line=line.replace("\n","")
                                quiz_info = line.split("\\")
                                if quiz_id==quiz_info[0]:
                                    print("quiz title : ",quiz_info[2])
                                    questions_ids = quiz_info[2]
                                    questions_ids_list = questions_ids.split(",")
                                    break
                        print("\nquiz questions\n")
                        counter=1
                        correct_answers=0
                        no_of_questions=len(questions_ids_list)
                        student_answers=[]
                        with open('Question.txt', 'r') as fp:
                            lines = fp.readlines()
                            for line in lines:
                                question_info=line.split("\\")
                                if (question_info[0] in questions_ids_list):
                                    question=question_info[1]
                                    answers=question_info[2].split(",")
                                    solution=question_info[3]
                                    print("Question ",counter)
                                    print("Question : ",question)
                                    print("a) ",answers[0])
                                    print("b) ",answers[1])
                                    print("c) ",answers[2])
                                    student_answer=input("Enter your solution (a/b/c) : ")
                                    student_answers.append(student_answer)
                                    if (student_answer.strip()==solution.strip()):
                                        print("\nCorrect!\n")
                                        correct_answers+=1
                                    else:
                                        print("\nWrong, Correct answer is : ",solution)
                                        print("\n")
                                    counter+=1
                        print(f"Your score is {correct_answers}/{no_of_questions}")
                        student_answers_content=",".join(student_answers)
                        with open('Student.txt', 'r') as fp:
                            lines = fp.readlines()
                            for line in lines:
                                student_info=line.split("\\")
                                if email==student_info[2]:              
                                    student_id=student_info[0]
                                    break
                        print(student_id)
                        print(quiz_id)
                        print(student_answers_content)
                        with open("Answer.txt", "a") as f:
                            f.write(student_id + "\\" + quiz_id + "\\" + student_answers_content + "\n")
                    else:
                        print("Please enter a correct option")
                    option=input("Do you want to finish ? (y/n) : ")
                    if (option=="y"):
                        exit=True
                    else:
                        exit=False
            elif EmailExistence == False:
                print("Email doesn't exist")
            else:
                print("Password is not correct")


    else:
        print("Please enter a valid option")
else:
    print("Please enter a valid option")



# In[ ]:




