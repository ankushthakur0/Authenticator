class SignUp:
    def __init__(self):
        print("Sign Up")


    def passwordChecker(self, password, confirmPassword):
        if password == confirmPassword:
            return True
        else:
            return False

    
    def doSignUp(self, firstName, LastName, age, emailAddress, password, confirmPassword):
        print("sign up")


        result = self.passwordChecker(password, confirmPassword)
        if result == True:
            print("Success!! ")
        else:
            print("Your Password does not match.. Try Again!! ")

    def checkExistance(self, emailAddress):
        pass

