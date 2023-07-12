def user_information(ussnm, pssd) :
    name = input("Enter you name please: ")
    address = input("Your address: ")
    age = input("Your age please: ")
    ussnm_ = ussnm+" task.txt"

    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address :")
    f.write(address)
    f.write('\n')
    f.write("Age: ")
    f.write(age)
    f.write('\n')
    f.close()

def login() :
    print("Please enter your username: ")
    user_nm = input("Enter here: ")

    pssd_wr = (input("enter the password")) + '\n'
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')
        k = f_.readline(0)[0]
        f_.close()

        if pssd_wr == k:
            print(
                "1--To view your data \n2--To add task \n3--Update\
                    task status \n4--View task status"
            )
            a = input()
            if a == '1':
                view_data(usernm)
            elif a == '2':
                task_information(usernm)
            elif a == '3':
                tas_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Wrong input!!! ")
        else:
            print("YOUR PASSSWORD OR USERNAME IS WRONG, TRY AGAIN")
            login()
    except Exception as e:
        print(e)
        login()

def signup() :
    print("Please enter the username by which you \
            wanna access your account")
    username = input("please enter here: ")
    password = input("Enter a password: ")
    user_information(username,password)
    print("Proceed to login... ")
    login()