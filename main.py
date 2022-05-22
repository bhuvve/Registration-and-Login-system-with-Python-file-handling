import os
import sys
import fileinput
"""
Register
"""
def register(Username=None, Password1=None, Password2=None):
    Username = input("Enter a username:")
    Password1 = input("Create password:")
    Password2 = input("Confirm Password:")
    db = open("database_file.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        d.append(a)
    if not len(Password1) < 8 and not len(Password1) > 16:
        db = open("database_file.txt", "r")
        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Username exists")
                register()
            elif guviUser(Username) is False:
                register()

            else:
                if Password1 == Password2:
                    special = num = upp = low = 0

                    for i in Password1:
                        string = "!@#$%^&*()"
                        if i in string:
                            special += 1
                        elif i.isupper():
                            upp += 1
                        elif i.islower():
                            low += 1
                        elif i in '1234567890':
                            num += 1

                    if special > 0:
                        if num > 0:
                            if upp > 0:
                                if low > 0:

                                    db = open("database_file.txt", "a")
                                    db.write(Username + ", " + str(Password1) + "\n")
                                    print("User created successfully!")
                                    print("Please login to proceed:")
                                else:
                                    print("Password must have one lowercase")
                                    register()
                            else:
                                print("Password must have one uppercase")
                                register()
                        else:
                            print("Password must have one number")
                            register()
                    else:
                        print("Password must have one special character", special)
                        register()

                # print(texts)
                else:
                    print("Passwords do not match")
                    register()
    else:
        print("Password too short")


def guviUser(Username):
    a = Username[0]
    a = a.lower()

    if '@.' in Username:
        print("Invalid Username" + " there should not be any " + "." + "immediate next to " + "@")
        return False

    if '@' not in Username or '.' not in Username:
        print("Invalid Username " + "It should like @domain.com or  @domain.in")
        return False

    elif 96 < ord(a) < 123:
        return True
    else:
        print("Username should not start with special characters and numbers")
        return False


##############################################
"""Login"""
def gainAccess(Username=None, Password=None):
    Username = input("Enter your username:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:
        if True:
            db = open("database_file.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))

            if Username in data:
                if Password == data[Username]:
                    print("Login success!")
                    print("Hi", Username)
                    print("Do you want to change Password"+"---> yes/no")
                    forpass = input()
                    if forpass == 'yes':
                        forget(data[Username])
                else:
                    print("Wrong password"+" --> Do you want to forget Password--> yes/no")
                    forpass = input()
                    if forpass== 'yes':
                        forget(data[Username])
            else:
                print("Username doesn't exist"+"  -->Do you want to register --> "+"yes/no")
                regkey=input()
                if regkey=='yes':
                    register()

        else:
            print("Error logging into the system")

    else:
        print("Please attempt login again")
        gainAccess()

 ##Forget Password


def forget(string1):
    existing_pass=string1
    Username = input("Enter a username:")
    Password1 = input("Enter new Password:")
    Password2 = input("Conform Password:")
    db = open("database_file.txt", "r")
    d = []

    if Password1 == Password2:
        special = num = upp = low = 0

        for i in Password1:
            string = "!@#$%^&*()"
            if i in string:
                special += 1
            elif i.isupper():
                upp += 1
            elif i.islower():
                low += 1
            elif i in '1234567890':
                num += 1

        if special > 0:
            if num > 0:
                if upp > 0:
                    if low > 0:
                        textToSearch = Username + ", " +existing_pass
                        textToReplace = Username + ", " + Password1
                        f = open("database_file.txt", 'r')
                        filedata = f.read()
                        f.close()
                        newdata = filedata.replace(textToSearch, textToReplace)
                        f = open("database_file.txt", 'w')
                        f.write(newdata)
                        f.close()
                    else:
                        print("Password must have one lowercase")
                        forget()
                else:
                    print("Password must have one uppercase")
                    forget()
            else:
                print("Password must have one number")
                forget()
        else:
             print("Password must have one special character")
             forget()




def welcome():
	print("Welcome, please select an option")
	option = input("Login | Signup:")
	if option == "Login":
		gainAccess()
	elif option == "Signup":
		register()
	else:
		print("Please enter a valid parameter, this is case-sensitive")


welcome()
