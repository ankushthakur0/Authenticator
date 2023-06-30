from Login import Login
from SignUp import SignUp

def welcome():
    print("Hello how are you! ")
    welcomeQuestion()


def welcomeQuestion():
    userInput = input(
        "Do you want to Login or Sign Up... \nPress L for Login and S for Sign Up")
    
    if (userInput == "L"):
        loginInput = Login()

        emailAddress = input("Enter Email Address")
        password = input("Enter Password")
        loginInput.doLogin(emailAddress, password)

    elif (userInput == "S"):
        SignUpInput = SignUp()

        firstName = input("Enter your First Name ")
        LastName = input("Enter your Last Name ")
        age = int(input("Enter you Age "))
        emailAddress = input("Enter your Email Address ")
        password = input("Enter your new password ")
        confirmPassword = input("Confirm Passqword ")
        SignUpInput.doSignUp(firstName, LastName, age, emailAddress, password, confirmPassword)

    else:
        print("Wrong Input!! ")
