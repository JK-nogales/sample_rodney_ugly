# # int - integers
# sample1 = 1

# sample2 = 35

# sample3 = 6.9

# #string - text, sentence
# sample4 = "rodeney said \"putang ina may dulo na kaagad\""
# print(sample4)

# #boolean - true or false lang siya 
# sample5 = True
# sample6 = False

# # formatted string print(f"hello {sample}!")


# name = input("what's your name? ")
# crush_name = input("what's your crush name? ") 


# print(f"{name} loves {crush_name} <3 ")

# ans = input("what is our first meal for tonight? (italian/japanese/chinese) ")

# if ans == "italian":
#     print("then eat fucking pizza! ")
# elif ans == "chinese":
#     print("then eat catdimsum! ")
# elif ans == "japanese":
#     print("then eat cencored sushi ")
# else:
#     print("INAVALID INPUT (MAGUTOM KA NA LANG TANGINA MO!) ")

# ans = int(input("how many hrs you sleep? "))

# if ans > 10:
#     print("gising kanmn")
# elif ans <= 10 and ans >= 8:
#     print("ayos tulog goods")
# elif ans <= 7:
#     print("tulog na")
# else:
#     print("shet")

# name_of_dreamJob = input("What's your dream job? ")
# YourName = input("what is your name? ")

# print(f" {YourName} Will be a succesfull {name_of_dreamJob} ")


# ans = input("are you going out for today? (yes/no)")

# if ans == "no":
#     print(" That's good enjoy the rest of your day! ")

# if ans == "yes":
#     ans1 = input(" what is the condition of the weather? (cloudy/sunny) ")
   
#     if ans1 == "cloudy":
#         print(" bring jacket and umbrella because the weather will be cold ")

#     elif ans1 == "sunny":
#         print(" wear light and fresh clothes ")


# else:
#     print(" WAG KANA UMALIS!!" *10 )


# ans = input( " HOW ARE YOU? ARE YOU OK? (YES/NO)")

# if ans == "NO":
#     ans1 = input(" REMEMBER THAT IM ALWAYS HERE, AND TOMMOROW IS ALWAYS A CHANCE TO HAVE A BETTER AND MEANINGFUL TOMORROW. can i know why? (YES/NO)")

#     if ans1 == "YES":
#         ans2 = input(" Go on tell me what happened, i will listen ")
       
#         print(" Don't worry we are always here for you luv yah <3 ")
        
#     elif ans1 == "NO":
#         print("ok hun, we are always here for you whenever you are ready love yah <3")

# elif ans == "YES":
#     print(" THATH'S GOOD TO HEAR LOVE, ALWYAS REMEMBER THAT IM ALWAYS HERE FOR YOU mwaaa <3")


# ans = input(" are you happy on your boyfriend rn (yes/no) ")

# if ans == "yes":


#     ans1 = input(" so do you see him in your future? (yes/no) ")
#     if ans1 == "no":
#         print(" ERROR TRY AGAIN! ")

#     elif ans1 == "yes":
#         ans2 = input(" are you willing to marry him? (yes/no)")
#         if ans2 == "no":
#             print(" ERROR TRY AGAIN!")

#         elif ans2 == "yes":
#             ans3 = input(" So will you marry me? -kelly <3 (yes/no)")
#             if ans3 =="no":
#                 print(" ERROR PLESE TRY AGAIN! ")
#             elif ans3 =="yes":
#                 print(" John Kelly Nogales and Jessielyn luisa Nogales are happily married!" )

# elif ans == "no":
#     print("ERROR PLEASE TRY AGAIN! ")

 
# name_OF_PLACE = input( " WHERE YOU AT NOW? " )
# name_of_the_person = input( " WHAT IS YOUR NAME? " )

# print(F"{name_of_the_person} IS AT {name_OF_PLACE}")


# feelings = input( "What do you feel rn after earlier? ")
# sequence = input( " what happened earlier is it your fault thats why you and jess haved a conflict? ")
# outcome = input( " DID ONE OF YOU TOLD SOMETHING TO EACH OTHER? ")

# print(F"I'M {feelings} WHY WHAT HAPPENED EATLIER? {sequence}, ohh i see so what happened after that? {outcome}")


# print(" the house is 1 million in price ")

# the_buyer_Have_Good_credit_true = False
# the_buyer_Have_Good_credit_False = True

# if the_buyer_Have_Good_credit_true:
#     print(" you only need to make a down payment of 10% ")
#     print(" $50 million ")

# elif the_buyer_Have_Good_credit_False:
#     print(" You have to make a down payment of 20% ")
#     print(" $100 million ")   


# feelings = input(" how are you now? ")
# sequence = input(" have you fully moved on? ")
# last = input(" how are you coping rn ")

# print(f"I'm {feelings} tell me what are you feeling rn are ok na? {sequence} I'm {last} ")

# import turtle  # Import the turtle module

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("white")  # Set the background color

# # Create a turtle object
# circle_turtle = turtle.Turtle()
# circle_turtle.color("blue")  # Set the color of the turtle's pen
# circle_turtle.speed(1)  # Set the drawing speed (1 is slow, 10 is fast)

# # Draw a circle
# circle_turtle.begin_fill()  # Start filling the shape
# circle_turtle.circle(100)  # Draw a circle with a radius of 100 units
# circle_turtle.end_fill()  # End filling the shape

# # Close the window when clicked
# screen.exitonclick()


# import turtle  # Import the turtle module

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("white")  # Set the background color to white

# # Create a turtle object
# flower_turtle = turtle.Turtle()
# flower_turtle.color("red")  # Set the color of the turtle's pen
# flower_turtle.speed(5)  # Set the drawing speed (1 is slow, 10 is fast)

# # Draw a flower by drawing multiple petals
# for _ in range(36):  # Loop to draw petals
#     flower_turtle.circle(100)  # Draw a circle with a radius of 100 units
#     flower_turtle.left(10)  # Rotate the turtle to the left by 10 degrees

# # Draw the stem
# flower_turtle.right(90)
# flower_turtle.color("green")
# flower_turtle.pensize(5)
# flower_turtle.forward(300)  # Draw a line for the stem

# # Close the window when clicked
# screen.exitonclick()


# import turtle  # Import the turtle module

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("white")  # Set the background color to white

# # Create a turtle object
# rose_turtle = turtle.Turtle()
# rose_turtle.speed(5)  # Set the drawing speed (1 is slow, 10 is fast)

# # Draw the petals of the rose
# rose_turtle.color("red")
# rose_turtle.begin_fill()
# for _ in range(36):  # Loop to draw multiple petals
#     rose_turtle.circle(100, 60)  # Draw a partial circle for the petal
#     rose_turtle.left(120)  # Rotate the turtle to the left
#     rose_turtle.circle(100, 60)  # Draw the opposite side of the petal
#     rose_turtle.left(10)  # Rotate slightly to create overlapping petals
# rose_turtle.end_fill()

# # Draw the stem
# rose_turtle.right(90)
# rose_turtle.color("green")
# rose_turtle.pensize(5)
# rose_turtle.forward(300)  # Draw a line for the stem

# # Draw leaves on the stem
# rose_turtle.penup()
# rose_turtle.setpos(0, -100)  # Move the turtle to the position to draw leaves
# rose_turtle.left(45)
# rose_turtle.pendown()
# rose_turtle.begin_fill()
# rose_turtle.circle(50, 90)  # Draw the first leaf
# rose_turtle.left(90)
# rose_turtle.circle(50, 90)
# rose_turtle.end_fill()

# rose_turtle.penup()
# rose_turtle.setpos(0, -200)  # Move the turtle to the position for the second leaf
# rose_turtle.right(135)
# rose_turtle.pendown()
# rose_turtle.begin_fill()
# rose_turtle.circle(50, 90)  # Draw the second leaf
# rose_turtle.left(90)
# rose_turtle.circle(50, 90)
# rose_turtle.end_fill()

# # Close the window when clicked
# screen.exitonclick()





