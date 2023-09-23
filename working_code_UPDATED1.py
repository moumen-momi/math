import random
import math
total_grade = 0
grade = 0
question_num = 0
question_num_right = 0 
question_num_wrong = 0
letter_list = ["A","B","C","D","E","F","G","H","Y","J"]
#game_intro
print("/"*12, "\n Welcome to Math Practice!", "\n ", "/"*12)
name_input = input(str(">>> Please Enter your name:"))
print("Hello", name_input,"!,Welcome to z game,\n","-"*20, "\n you will get tested on your skills on area, volume/permitre with 2 questions per shape! \n You have 3 points per shape, while you got a second chance you may get penalized or get a mark deducted if a HINT is used.\n","-"*20)
def game_choice():
    user_choice = input("Do you want to (choose) a shape or (random)?")
    if user_choice.lower().startswith("c"):
        print("Choose a Shape from the following:\n","-"*20, "\nNote: choose shape by inputting CAPITAL letter assotiated with it!\n","-"*20)
        print("A.Square\nB.Circle\nC.Triangle\nD.Rectangle\nE.Cube\nF.Sphere\nG.Rectangular Solid\nH.Cylinder\nY.Square Pyramid\nJ.Pentagon\n","-"*20)
        choice = input(">")
    elif user_choice.lower().startswith("r"):
        choice = random.choice(letter_list)
    else:
        print("Wrong input!, Please try again!")
        game_choice()
    if choice == "A":
        sqr()
    if choice == "B":
        crkl()
    if choice == "C":
        tri()
    if choice == "D":
        rktngl()
    if choice == "E":
        cube()
    if choice == "F":
        sphyr()
    if choice == "G":
        sld_rktngl()
    if choice == "H":
        cylndr()
    if choice == "Y":
        pyrmd()
    if choice == "J":
        penta()
    else:
        print("Thats not one of the choices!\nPlease try again!")
        game_choice()
    game_choice()
def sld_rktngl():
    global question_num
    global question_num_right
    global question_num_wrong
    global total_grade
    global grade
    sld_rktngl_length = random.randint(51,75)
    sld_rktngl_width = random.randint(10, 50)
    sld_rktngl_height = random.randint(51,75)
    sld_rktngl_area = round((2*((sld_rktngl_width*sld_rktngl_length)+(sld_rktngl_height*sld_rktngl_length)+(sld_rktngl_height*sld_rktngl_width))))
    sld_rktngl_volume = round(sld_rktngl_width*sld_rktngl_height*sld_rktngl_length)
    #print(sld_rktngl_length, sld_rktngl_height, sld_rktngl_width, sld_rktngl_volume, sld_rktngl_area)
    print("Welcome to your challenge!, \n A Rectangular Solid has length of", sld_rktngl_length, "units and width of", sld_rktngl_width," units and height of", sld_rktngl_height, "units. \n Find the area and volume of the Solid. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade+=3
    question_num+=1 
    sld_rktngl_area_input = int(input("Enter the area value:"))
    sld_rktngl_volume_input = int(input("Enter the volume:"))
    if sld_rktngl_area_input == sld_rktngl_area and sld_rktngl_volume_input == sld_rktngl_volume:
        print("Congrats! You survived the challenge!\n The area is", sld_rktngl_area,"And the volume is", sld_rktngl_volume, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif sld_rktngl_area_input != sld_rktngl_area and sld_rktngl_volume_input == sld_rktngl_volume:
        print("Sorry, only the volume given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sld_rktngl_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sld_rktngl_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Rectangle formula is : 2(wl+hl+hw) ")
        elif sld_rktngl_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of Rectangular Solid with length", sld_rktngl_length, "units and width", sld_rktngl_width, "units and height of", sld_rktngl_height, "units")
        sld_rktngl_area_input_area_wrong = int(input("Enter the area value:"))
        if sld_rktngl_area_input_area_wrong == sld_rktngl_area:
            print("Congrats! You got the area value right which is", sld_rktngl_area)
            if sld_rktngl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif sld_rktngl_area_input == sld_rktngl_area and sld_rktngl_volume_input != sld_rktngl_volume_input_2:
        print("Sorry, only the area given is right while the volume is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sld_rktngl_hint_input_volume_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sld_rktngl_hint_input_volume_wrong.lower().startswith("y"):
            print("Hint: The volume of Rectangle formula is : whl ")
        elif sld_rktngl_hint_input_volume_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the volume of Rectangular Solid with length of", sld_rktngl_length, "units and width of", sld_rktngl_width, "units and height of", sld_rktngl_height,"units.")
        sld_rktngl_volume_input_volume_wrong = int(input("Enter volume's value:"))
        if sld_rktngl_volume_input_volume_wrong == sld_rktngl_volume:
            print("Congrats! You got the volume value right which is", sld_rktngl_volume)
            if sld_rktngl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        sld_rktngl_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if sld_rktngl_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Rectangular Solid is : 2(wl+hl+hw) \n And volume of Rectangular Solid is: whl")
        elif sld_rktngl_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and volume of Rectangular Solid with length", sld_rktngl_length, "units and width of", sld_rktngl_width, "units and height of", sld_rktngl_height,"units")
        sld_rktngl_area_input_2 = int(input("Enter the area value:"))
        sld_rktngl_volume_input_2 = int(input("Enter the volume:"))
        if sld_rktngl_area_input_2 == sld_rktngl_area and sld_rktngl_volume_input_2 == sld_rktngl_volume :
            print("Congrats! You survived the challenge!" )
            if sld_rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif sld_rktngl_area_input_2 != sld_rktngl_area and sld_rktngl_volume_input_2 == sld_rktngl_volume:
            print("Sorry, only the volume was right while the area answer was wrong. As it was", sld_rktngl_area, "units")
            if sld_rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif sld_rktngl_area_input_2 == sld_rktngl_area and sld_rktngl_volume_input_2 != sld_rktngl_volume:
            print("Sorry, only the area was right while the volume was wrong as it was", sld_rktngl_volume, "units.")
            if sld_rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", sld_rktngl_area , "units and the volume was", sld_rktngl_volume, "units and height of", sld_rktngl_height,"units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def tri():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    tri_side_1 = random.randint(20,39)
    tri_side_2 = random.randint(20,39)
    tri_side_3 = random.randint(20,39)
    #cond = tri_side_1+tri_side_2>tri_side_3 and tri_side_1+tri_side_3>tri_side_2 and tri_side_2+tri_side_3>tri_side_1
    #while cond:
        #print(tri_side_1, tri_side_2, tri_side_3)
        #break
    #print( "Yes!", tri_side_1 + tri_side_2 + tri_side_3 )
    third_side_angle = round(math.acos((tri_side_1**2+tri_side_2**2- tri_side_3**2)/(2*tri_side_1*tri_side_2)))
    tri_permetre = round(tri_side_1 + tri_side_2 + tri_side_3)
    tri_area = round((0.5*tri_side_1*tri_side_2*(math.sin(third_side_angle))))
    print("Welcome to your challenge!, \n A Triangle has 3 sides with length", tri_side_1, tri_side_2, "and" ,tri_side_3, "units, repectively. While angle of 3rd side is", third_side_angle, "\n Find the area and permetre of the Triangle. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    tri_area_input = int(input("Enter the area value:"))
    tri_permetre_input = int(input("Enter the permetre:"))
    if tri_area_input == tri_area and tri_permetre_input == tri_permetre:
        print("Congrats! You survived the challenge!\n The area is", tri_area,"And the permetre is", tri_permetre, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif tri_area_input != tri_area and tri_permetre_input == tri_permetre:
        print("Sorry, only the permetre given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        tri_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if tri_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Triangle formula is : 0.5(A x B x SinC) ")
        elif tri_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of the Triangle with sides of length", tri_side_1, tri_side_2, tri_side_3, "units respectively, while 3rd sid angle is about", third_side_angle, "degrees")
        tri_area_input_area_wrong = int(input("Enter the area value:"))
        if tri_area_input_area_wrong == tri_area:
            print("Congrats! You got the area value right which is", tri_area)
            if tri_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif tri_area_input == tri_area and tri_permetre_input != tri_permetre_input_2:
        print("Sorry, only the area given is right while the permetre is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        tri_hint_input_permetre_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if tri_hint_input_permetre_wrong.lower().startswith("y"):
            print("Hint: The permetre of Triangle formula is : A + B + C ")
        elif tri_hint_input_permetre_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the permetre of Triangle with sides of length",tri_side_1, tri_side_2, tri_side_3 , "units, respectively while the 3rd angle is about", third_side_angle, "degrees")
        tri_permetre_input_permetre_wrong = int(input("Enter permetre's value:"))
        if tri_permetre_input_permetre_wrong == tri_permetre:
            print("Congrats! You got the permetre value right which is", tri_permetre)
            if tri_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_wrong+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        tri_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if tri_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Triangle is : 0.5(A x B x SinC) \n And permetre of Triangle is: A + B + C")
        elif tri_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and permetre of Triangle with sides of length", tri_side_1, tri_side_2, tri_side_3, "units, respectively while 3rd side has an angle at about", third_side_angle, "degrees.")
        tri_area_input_2 = int(input("Enter the area value:"))
        tri_permetre_input_2 = int(input("Enter the permetre:"))
        if tri_area_input_2 == tri_area and tri_permetre_input_2 == tri_permetre :
            print("Congrats! You survived the challenge!" )
            if tri_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif tri_area_input_2 != tri_area and tri_permetre_input_2 == tri_permetre:
            print("Sorry, only the permetre was right while the area answer was wrong. As it was", tri_area, "units")
            if tri_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif tri_area_input_2 == tri_area and tri_permetre_input_2 != tri_permetre:
            print("Sorry, only the area was right while the permetre was wrong as it was", tri_permetre, "units.")
            if tri_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", tri_area , "units and the permetre was", tri_permetre, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def sqr():
    global question_num
    global question_num_right
    global question_num_wrong
    global total_grade
    global grade
    sqr_side = random.randint(5,100)
    sqr_permetre = round(sqr_side*4)
    sqr_area = round(sqr_side**2)
    #print(sqr_side, sqr_permiter, sqr_area)
    print("Welcome to your challenge!, \n A Square has side length", sqr_side, "units \n Find the area and permetre of the square. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    sqr_area_input = int(input("Enter the area value:"))
    sqr_permetre_input = int(input("Enter the permetre:"))
    if sqr_area_input == sqr_area and sqr_permetre_input == sqr_permetre:
        print("Congrats! You survived the challenge!\n The area is", sqr_area,"And the permetre is", sqr_permetre, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif sqr_area_input != sqr_area and sqr_permetre_input == sqr_permetre:
        print("Sorry, only the permetre given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sqr_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sqr_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Square formula is : Side^2 ")
        elif sqr_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of Square with side(s) of length", sqr_side, "units")
        sqr_area_input_area_wrong = int(input("Enter the area value:"))
        if sqr_area_input_area_wrong == sqr_area:
            print("Congrats! You got the area value right which is", sqr_area, "\n You could now proceed to next question or choose to END?")
            if sqr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    elif sqr_area_input == sqr_area and sqr_permetre_input != sqr_permetre_input_2:
        print("Sorry, only the area given is right while the permetre is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sqr_hint_input_permetre_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sqr_hint_input_permetre_wrong.lower().startswith("y"):
            print("Hint: The permetre of square formula is : 4(side) ")
        elif sqr_hint_input_permetre_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the permetre of Square with side length of", sqr_side, "units")
        sqr_permetre_input_permetre_wrong = int(input("Enter permetre's value:"))
        if sqr_permetre_input_permetre_wrong == sqr_permetre:
            print("Congrats! You got the permetre value right which is", sqr_permetre, "\n You could now proceed to next question or choose to END?")
            if sqr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        sqr_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if sqr_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of square is : side^2 \n And permetre of square is: 4(side)")
        elif sqr_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and permetre of Square with side(s) of length", sqr_side, "units")
        sqr_area_input_2 = int(input("Enter the area value:"))
        sqr_permetre_input_2 = int(input("Enter the permetre:"))
        if sqr_area_input_2 == sqr_area and sqr_permetre_input_2 == sqr_permetre :
            print("Congrats! You survived the challenge!" )
            if sqr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif sqr_area_input_2 != sqr_area and sqr_permetre_input_2 == sqr_permetre:
            print("Sorry, only the permetre was right while the area answer was wrong. As it was", sqr_area, "units")
            if sqr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif sqr_area_input_2 == sqr_area and sqr_permetre_input_2 != sqr_permetre:
            print("Sorry, only the area was right while the permetre was wrong as it was", sqr_permetre, "units.")
            if sqr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", sqr_area , "units and the permetre was", sqr_permetre, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def sphyr():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    sphyr_radius = random.randrange(5,100)
    sphyr_area = round(4*math.pi*sphyr_radius**2)
    sphyr_volume = round(((4/3) * math.pi * sphyr_radius**3))
    #print(sphyr_radius, sphyr_area, sphyr_vol)
    print("Welcome to your challenge!, \n A Sphere has radius length", sphyr_radius, "units \n Find the area and volume of the Sphere. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    sphyr_area_input = int(input("Enter the area value:"))
    sphyr_volume_input = int(input("Enter the volume:"))
    if sphyr_area_input == sphyr_area and sphyr_volume_input == sphyr_volume:
        print("Congrats! You survived the challenge!\n The area is", sphyr_area,"And the volume is", sphyr_volume, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif sphyr_area_input != sphyr_area and sphyr_volume_input == sphyr_volume:
        print("Sorry, only the volume given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sphyr_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sphyr_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Sphere formula is : 4πr^2 ")
        elif sphyr_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of Sphere with radius of length", sphyr_radius, "units")
        sphyr_area_input_area_wrong = int(input("Enter the area value:"))
        if sphyr_area_input_area_wrong == sphyr_area:
            print("Congrats! You got the area value right which is", sphyr_area)
            if sphyr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif sphyr_area_input == sphyr_area and sphyr_volume_input != sphyr_volume_input_2:
        print("Sorry, only the area given is right while the volume is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        sphyr_hint_input_volume_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if sphyr_hint_input_volume_wrong.lower().startswith("y"):
            print("Hint: The volume of Sphere formula is : 4/3πr^3 ")
        elif sphyr_hint_input_volume_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the volume of Sphere with radius length of", sphyr_radius, "units")
        sphyr_volume_input_volume_wrong = int(input("Enter volume's value:"))
        if sphyr_volume_input_volume_wrong == sphyr_volume:
            print("Congrats! You got the volume value right which is", sphyr_volume)
            if sphyr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        sphyr_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if sphyr_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Sphere is : 4πr^2 \n And volume of Sphere is: 4/3πr^3")
        elif sphyr_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and volume of Sphere with radius of length", sphyr_radius, "units")
        sphyr_area_input_2 = int(input("Enter the area value:"))
        sphyr_volume_input_2 = int(input("Enter the volume:"))
        if sphyr_area_input_2 == sphyr_area and sphyr_volume_input_2 == sphyr_volume :
            print("Congrats! You survived the challenge!" )
            if sphyr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif sphyr_area_input_2 != sphyr_area and sphyr_volume_input_2 == sphyr_volume:
            print("Sorry, only the volume was right while the area answer was wrong. As it was", sphyr_area, "units")
            if sphyr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif sphyr_area_input_2 == sphyr_area and sphyr_volume_input_2 != sphyr_volume:
            print("Sorry, only the area was right while the volume was wrong as it was", sphyr_volume, "units.")
            if sphyr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", sphyr_area , "units and the volume was", sphyr_volume, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def rktngl():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    rktngl_length = random.randint(50,100)
    rktngl_width = random.randint(10, 50)
    rktngl_permetre = round(2*(rktngl_length+rktngl_width))
    rktngl_area = round(rktngl_length*rktngl_width)
    #print(rktngl_width, rktngl_length, rktngl_permiter, rktngl_area)
    print("Welcome to your challenge!, \n A Rectangle has length of", rktngl_length, "units and width of", rktngl_width," units \n Find the area and permetre of the Rectangle. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    rktngl_area_input = int(input("Enter the area value:"))
    rktngl_permetre_input = int(input("Enter the permetre:"))
    if rktngl_area_input == rktngl_area and rktngl_permetre_input == rktngl_permetre:
        print("Congrats! You survived the challenge!\n The area is", rktngl_area,"And the permetre is", rktngl_permetre, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif rktngl_area_input != rktngl_area and rktngl_permetre_input == rktngl_permetre:
        print("Sorry, only the permetre given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        rktngl_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if rktngl_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Rectangle formula is : Length x Width ")
        elif rktngl_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of Rectangle with length", rktngl_length, "units and width", rktngl_width, "units.")
        rktngl_area_input_area_wrong = int(input("Enter the area value:"))
        if rktngl_area_input_area_wrong == rktngl_area:
            print("Congrats! You got the area value right which is", rktngl_area)
            if rktngl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif rktngl_area_input == rktngl_area and rktngl_permetre_input != rktngl_permetre_input_2:
        print("Sorry, only the area given is right while the permetre is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        rktngl_hint_input_permetre_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if rktngl_hint_input_permetre_wrong.lower().startswith("y"):
            print("Hint: The permetre of Rectangle formula is : 2 x ( Length + Width ) ")
        elif rktngl_hint_input_permetre_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the permetre of Rectangle with length of", rktngl_length, "units and width of", rktngl_width, "units.")
        rktngl_permetre_input_permetre_wrong = int(input("Enter permetre's value:"))
        if rktngl_permetre_input_permetre_wrong == rktngl_permetre:
            print("Congrats! You got the permetre value right which is", rktngl_permetre)
            if rktngl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        rktngl_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if rktngl_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Rectangle is : Length x Width \n And permetre of Rectangle is: 2 x (Length + Width)")
        elif rktngl_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and permetre of Rectangle with length", rktngl_length, "units and width of", rktngl_width, "units")
        rktngl_area_input_2 = int(input("Enter the area value:"))
        rktngl_permetre_input_2 = int(input("Enter the permetre:"))
        if rktngl_area_input_2 == rktngl_area and rktngl_permetre_input_2 == rktngl_permetre :
            print("Congrats! You survived the challenge!" )
            if rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif rktngl_area_input_2 != rktngl_area and rktngl_permetre_input_2 == rktngl_permetre:
            print("Sorry, only the permetre was right while the area answer was wrong. As it was", rktngl_area, "units")
            if rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif rktngl_area_input_2 == rktngl_area and rktngl_permetre_input_2 != rktngl_permetre:
            print("Sorry, only the area was right while the permetre was wrong as it was", rktngl_permetre, "units.")
            if rktngl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", rktngl_area , "units and the permetre was", rktngl_permetre, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def pyrmd():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    pyrmd_base_edge = random.randint(5,100)
    pyrmd_height = random.randint(15,100)
    pyrmd_area = round(((pyrmd_base_edge**2)+(2*pyrmd_base_edge)*(math.sqrt((pyrmd_base_edge**2/4)+pyrmd_height**2))))
    pyrmd_vol = round(((pyrmd_base_edge**2)*(pyrmd_height/3)))
    #print(pyrmd_base_edge, pyrmd_height, pyrmd_area, pyrmd_vol)
    print("Welcome to your challenge!, \n A Square Pyramid has base edge with length", pyrmd_base_edge, "units and highet of", pyrmd_height, "units. \n Find the area and volume of the given shape. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    pyrmd_area_input = int(input("Enter the Surface area value:"))
    pyrmd_vol_input = int(input("Enter the volume:"))
    if pyrmd_area_input == pyrmd_area and pyrmd_vol_input == pyrmd_vol:
        print("Congrats! You survived the challenge!\n The area is", pyrmd_area,"And the volume is", pyrmd_vol, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif pyrmd_area_input != pyrmd_area and pyrmd_vol_input == pyrmd_vol:
        print("Sorry, only the volume given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        pyrmd_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if pyrmd_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of pyramid formula is : a^2+2a√a^2/4+h^2 ")
        elif pyrmd_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Surface Area of Square Pyramid with base edge of length", pyrmd_base_edge, "and height", pyrmd_height, "units.")
        pyrmd_area_input_area_wrong = int(input("Enter the Surface area value:"))
        if pyrmd_area_input_area_wrong == pyrmd_area:
            print("Congrats! You got the area value right which is", pyrmd_area, "\n You could now proceed to next question or choose to END?")
            if pyrmd_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    elif pyrmd_area_input == pyrmd_area and pyrmd_vol_input != pyrmd_vol_input_2:
        print("Sorry, only the area given is right while the volume is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        pyrmd_hint_input_volume_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if pyrmd_hint_input_volume_wrong.lower().startswith("y"):
            print("Hint: The volume of pyramid formula is :  a^2(h/3) ")
        elif pyrmd_hint_input_volume_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Volume of Square Pyramid with base edge of length", pyrmd_base_edge, "and height", pyrmd_height, "units.")
        pyrmd_volume_input_volume_wrong = int(input("Enter volume's value:"))
        if pyrmd_volume_input_volume_wrong == pyrmd_vol:
            print("Congrats! You got the area value right which is", pyrmd_vol, "\n You could now proceed to next question or choose to END?")
            if pyrmd_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        pyrmd_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if pyrmd_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of pyramid formula is : a^2+2a√a^2/4+h^2 \n And volume of pyramid formula is: a^2(h/3)")
        elif pyrmd_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Surface Area and Volume of Square Pyramid with base edge of length", pyrmd_base_edge, "and height", pyrmd_height, "units.")
        pyrmd_area_input_2 = int(input("Enter the Surface area value:"))
        pyrmd_vol_input_2 = int(input("Enter the volume:"))
        if pyrmd_area_input_2 == pyrmd_area and pyrmd_vol_input_2 == pyrmd_vol :
            print("Congrats! You survived the challenge!" )
            if pyrmd_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif pyrmd_area_input_2 != pyrmd_area and pyrmd_vol_input_2 == pyrmd_vol:
            print("Sorry, only the volume was right while the area answer was wrong. As it was", pyrmd_area, "units")
            if pyrmd_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif pyrmd_area_input_2 == pyrmd_area and pyrmd_vol_input_2 != pyrmd_vol:
            print("Sorry, only the area was right while the volume was wrong as it was", pyrmd_vol, "units.")
            if pyrmd_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", pyrmd_area , "units and the volume was", pyrmd_vol, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def cylndr():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    cylndr_radius = random.randrange(5,100)
    cylndr_height = random.randrange(10,80)
    cylndr_area = round(((2*math.pi*cylndr_radius*cylndr_height) + (2*math.pi*cylndr_radius**2)))
    cylndr_vol = round((math.pi*(cylndr_radius**2)*cylndr_height))
    #print(cylndr_radius, cylndr_height, cylndr_area, cylndr_vol)
    print("Welcome to your challenge!, \n A Cylender has radius with length", cylndr_radius, "units and highet of", cylndr_height, "units. \n Find the area and volume of the given shape. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    cylndr_area_input = int(input("Enter the area value:"))
    cylndr_vol_input = int(input("Enter the volume:"))
    if cylndr_area_input == cylndr_area and cylndr_vol_input == cylndr_vol:
        print("Congrats! You survived the challenge!\n The area is", cylndr_area,"And the volume is", cylndr_vol, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif cylndr_area_input != cylndr_area and cylndr_vol_input == cylndr_vol:
        print("Sorry, only the volume given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        cylndr_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if cylndr_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Cylender formula is : 2πrh+2πr^2 ")
        elif cylndr_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of the Cylender with radius of length", cylndr_radius, "and height", cylndr_height, "units.")
        cylndr_area_input_area_wrong = int(input("Enter the area value:"))
        if cylndr_area_input_area_wrong == cylndr_area:
            print("Congrats! You got the area value right which is", cylndr_area)
            if cylndr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif cylndr_area_input == cylndr_area and cylndr_vol_input != cylndr_vol_input_2:
        print("Sorry, only the area given is right while the volume is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        cylndr_hint_input_volume_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if cylndr_hint_input_volume_wrong.lower().startswith("y"):
            print("Hint: The volume of Cylender formula is :  πr^2h ")
        elif cylndr_hint_input_volume_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Volume of Cylender with radius of length", cylndr_radius, "and height", cylndr_height, "units.")
        cylndr_volume_input_volume_wrong = int(input("Enter volume's value:"))
        if cylndr_volume_input_volume_wrong == cylndr_vol:
            print("Congrats! You got the area value right which is", cylndr_vol)
            if cylndr_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        cylndr_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if cylndr_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Cylender formula is : 2πrh+2πr^2 \n And volume of Cylender formula is: πr^2h")
        elif cylndr_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and Volume of Cylender with radius of length", cylndr_radius, "and height", cylndr_height, "units.")
        cylndr_area_input_2 = int(input("Enter the area value:"))
        cylndr_vol_input_2 = int(input("Enter the volume:"))
        if cylndr_area_input_2 == cylndr_area and cylndr_vol_input_2 == cylndr_vol :
            print("Congrats! You survived the challenge!" )
            if cylndr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif cylndr_area_input_2 != cylndr_area and cylndr_vol_input_2 == cylndr_vol:
            print("Sorry, only the volume was right while the area answer was wrong. As it was", cylndr_area, "units")
            if cylndr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif cylndr_area_input_2 == cylndr_area and cylndr_vol_input_2 != cylndr_vol:
            print("Sorry, only the area was right while the volume was wrong as it was", cylndr_vol, "units.")
            if cylndr_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", cylndr_area , "units and the volume was", cylndr_vol, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def cube():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    cube_side = random.randint(5,100)
    cube_area = round(6*cube_side**2)
    cube_volume = round(cube_side**3)
    #print(cube_side, cube_area, cube_volume)
    print("Welcome to your challenge!, \n A cube has side length", cube_side, "units \n Find the area and volume of the cube. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    cube_area_input = int(input("Enter the area value:"))
    cube_volume_input = int(input("Enter the volume:"))
    if cube_area_input == cube_area and cube_volume_input == cube_volume:
        print("Congrats! You survived the challenge!\n The area is", cube_area,"And the volume is", cube_volume, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif cube_area_input != cube_area and cube_volume_input == cube_volume:
        print("Sorry, only the volume given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        cube_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if cube_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of cube formula is : 6a^2 ")
        elif cube_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of cube with side(s) of length", cube_side, "units")
        cube_area_input_area_wrong = int(input("Enter the area value:"))
        if cube_area_input_area_wrong == cube_area:
            print("Congrats! You got the area value right which is", cube_area, "\n You could now proceed to next question or choose to END?")
            if cube_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    elif cube_area_input == cube_area and cube_volume_input != cube_volume_input_2:
        print("Sorry, only the area given is right while the volume is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        cube_hint_input_volume_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if cube_hint_input_volume_wrong.lower().startswith("y"):
            print("Hint: The volume of cube formula is : a^3 ")
        elif cube_hint_input_volume_wrong.lower().startswith("y"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the volume of cube with side length of", cube_side, "units")
        cube_volume_input_volume_wrong = int(input("Enter volume's value:"))
        if cube_volume_input_volume_wrong == cube_volume:
            print("Congrats! You got the volume value right which is", cube_volume, "\n You could now proceed to next question or choose to END?")
            if cube_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question. \n Would you like to continue to the next challenge or END?")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        cube_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if cube_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of cube is : 6a^2 \n And volume of cube is: a^3")
        elif cube_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and volume of cube with side(s) of length", cube_side, "units")
        cube_area_input_2 = int(input("Enter the area value:"))
        cube_volume_input_2 = int(input("Enter the volume:"))
        if cube_area_input_2 == cube_area and cube_volume_input_2 == cube_volume :
            print("Congrats! You survived the challenge!" )
            if cube_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif cube_area_input_2 != cube_area and cube_volume_input_2 == cube_volume:
            print("Sorry, only the volume was right while the area answer was wrong. As it was", cube_area, "units")
            if cube_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif cube_area_input_2 == cube_area and cube_volume_input_2 != cube_volume:
            print("Sorry, only the area was right while the volume was wrong as it was", cube_volume, "units.")
            if cube_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", cube_area , "units and the volume was", cube_volume, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def crkl():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    crkl_radius = random.randrange(5,100)
    crkl_circumference = round(2*math.pi*crkl_radius)
    crkl_area = round(math.pi*crkl_radius**2)
    #print(crkl_radius, crkl_circumference, crkl_area)
    print("Welcome to your challenge!, \n A Circle has radius of", crkl_radius, "units. \n Find the area and circumference of the Circle. \n Make sure to answer using a number rounded to the nearest unit/figure")
    total_grade = total_grade + 3
    question_num+=1
    crkl_area_input = int(input("Enter the area value:"))
    crkl_circumference_input = int(input("Enter the circumference:"))
    if crkl_area_input == crkl_area and crkl_circumference_input == crkl_circumference:
        print("Congrats! You survived the challenge!\n The area is", crkl_area,"And the circumference is", crkl_circumference, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif crkl_area_input != crkl_area and crkl_circumference_input == crkl_circumference:
        print("Sorry, only the circumference given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        crkl_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if crkl_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Circle formula is : πr^2 ")
        elif crkl_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of the Circle with radius", crkl_radius, "units")
        crkl_area_input_area_wrong = int(input("Enter the area value:"))
        if crkl_area_input_area_wrong == crkl_area:
            print("Congrats! You got the area value right which is", crkl_area)
            if crkl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif crkl_area_input == crkl_area and crkl_circumference_input != crkl_circumference_input_2:
        print("Sorry, only the area given is right while the circumference is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        crkl_hint_input_circumference_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if crkl_hint_input_circumference_wrong.lower().startswith("y"):
            print("Hint: The circumference of Circle formula is : 2πr ")
        elif crkl_hint_input_circumference_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the circumference of Circle with radius of", crkl_radius, "units")
        crkl_circumference_input_circumference_wrong = int(input("Enter circumference's value:"))
        if crkl_circumference_input_circumference_wrong == crkl_circumference:
            print("Congrats! You got the circumference value right which is", crkl_circumference)
            if crkl_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        crkl_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if crkl_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of Circle is : πr^2 \n And circumference of Circle is: 2πr")
        elif crkl_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and circumference of Circle with radius", crkl_radius, "units")
        crkl_area_input_2 = int(input("Enter the area value:"))
        crkl_circumference_input_2 = int(input("Enter the circumference:"))
        if crkl_area_input_2 == crkl_area and crkl_circumference_input_2 == crkl_circumference :
            print("Congrats! You survived the challenge!" )
            if crkl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif crkl_area_input_2 != crkl_area and crkl_circumference_input_2 == crkl_circumference:
            print("Sorry, only the circumference was right while the area answer was wrong. As it was", crkl_area, "units")
            if crkl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif crkl_area_input_2 == crkl_area and crkl_circumference_input_2 != crkl_circumference:
            print("Sorry, only the area was right while the circumference was wrong as it was", crkl_circumference, "units.")
            if crkl_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", crkl_area , "units and the circumference was", crkl_circumference, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
def penta():
    global total_grade
    global question_num
    global question_num_right
    global question_num_wrong
    global grade
    total_grade+=3
    question_num+=1
    penta_side = random.randint(5,100)
    penta_area = round((1/4*(math.sqrt(5*(5+2*math.sqrt(5))))*penta_side**2))
    penta_permetre = round(5*penta_side)
    #print(penta_side, penta_area, penta_permetre)
    print("Welcome to your challenge!, \n A Pentagon has side length", penta_side, "units \n Find the area and permetre of the Pentagon. \n Make sure to answer using a number rounded to the nearest unit/figure")
    penta_area_input = int(input("Enter the area value:"))
    penta_permetre_input = int(input("Enter the permetre:"))
    if penta_area_input == penta_area and penta_permetre_input == penta_permetre:
        print("Congrats! You survived the challenge!\n The area is", penta_area,"And the permetre is", penta_permetre, "\n Hence, contributing to your career development by 3 points!")
        grade = grade + 3
        question_num_right+=1
    elif penta_area_input != penta_area and penta_permetre_input == penta_permetre:
        print("Sorry, only the permetre given is right while the area is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        penta_hint_input_area_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if penta_hint_input_area_wrong.lower().startswith("y"):
            print("Hint: The area of Pentagon formula is : 1/4√(5+2√5)a^2 ")
        elif penta_hint_input_area_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area of Pentagon with side(s) of length", penta_side, "units")
        penta_area_input_area_wrong = int(input("Enter the area value:"))
        if penta_area_input_area_wrong == penta_area:
            print("Congrats! You got the area value right which is", penta_area)
            if penta_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    elif penta_area_input == penta_area and penta_permetre_input != penta_permetre_input_2:
        print("Sorry, only the area given is right while the permetre is wrong. \n Thus you are given a second chance to retrieve lost point(s)")
        penta_hint_input_permetre_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2\n Please answer in form of (Yes) or (No) "))
        if penta_hint_input_permetre_wrong.lower().startswith("y"):
            print("Hint: The permetre of Pentagon formula is : 5a ")
        elif penta_hint_input_permetre_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the permetre of Pentagon with side length of", penta_side, "units")
        penta_permetre_input_permetre_wrong = int(input("Enter permetre's value:"))
        if penta_permetre_input_permetre_wrong == penta_permetre:
            print("Congrats! You got the permetre value right which is", penta_permetre)
            if penta_hint_input_area_wrong.lower().startswith("y"):
                grade = grade + 2
                question_num_right+=1
            else:
                grade = grade + 3
                question_num_right+=1
        else:
            print("Sorry the answer given was not right. \n Therefore, loosing your last attempt at solving the question.")
            grade = grade + 1
            question_num_wrong+=1
    else:
        print("Sorry both answers given was not right. \n Thus, you are given an extra chance.")
        penta_hint_input_all_wrong = str(input("Would you like a hint to help? \n Note: A hint would decrease your earned points to be 1 rather than 2 (with panalisation of original 3) whilst you must answer both questions right to recieve the point \n Please answer in form of (Yes) or (No) "))
        if penta_hint_input_all_wrong.lower().startswith("y"):
            print("Hint: The area of square is : 1/4√(5+2√5)a^2 \n And permetre of square is: 5a")
        elif penta_hint_input_all_wrong.lower().startswith("n"):
            print("Kudos for choosing to aim for more points over assistance!")
        else:
            print("As wrong input was given the hint will be automaticaly discarded")
        print("Seocnd chance: \n You could still recover some of point(s) from the question! \n As a reminder find the Area and permetre of Pentagon with side(s) of length", penta_side, "units")
        penta_area_input_2 = int(input("Enter the area value:"))
        penta_permetre_input_2 = int(input("Enter the permetre:"))
        if penta_area_input_2 == penta_area and penta_permetre_input_2 == penta_permetre :
            print("Congrats! You survived the challenge!" )
            if penta_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 1
                question_num_right+=1
            else:
                grade = grade + 2
                question_num_right+=1
        elif penta_area_input_2 != penta_area and penta_permetre_input_2 == penta_permetre:
            print("Sorry, only the permetre was right while the area answer was wrong. As it was", penta_area, "units")
            if penta_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        elif penta_area_input_2 == penta_area and penta_permetre_input_2 != penta_permetre:
            print("Sorry, only the area was right while the permetre was wrong as it was", penta_permetre, "units.")
            if penta_hint_input_all_wrong.lower().startswith("y"):
                grade = grade + 0
                question_num_wrong+=1
            else:
                grade = grade + 1
                question_num_wrong+=1
        else:
            print("Sorry all the answers given was not right. \n Therefore, loosing your last attempt at solving the question. \n The area was", penta_area , "units and the permetre was", penta_permetre, "units")
            grade = grade + 0
            question_num_wrong+=1
    answer = input('Do you want to continue to the next challenge??:')
    while True:
        if answer.lower().startswith("n"):
            print("Ok, your grade is", grade,"/",total_grade,".\n Congrats, looking forward to meeting you in the next round!")
            exit()
        
        elif answer.lower().startswith("y"):
            break
    game_choice()
game_choice()