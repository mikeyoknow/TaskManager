import datetime

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
                task_update(user_nm)
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

def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()

def task_information(username):
    print("Enter number of task you'd like to add: ")
    j = int(input())
    f1 = open(username, 'a')

    for i in range (1, j+1):
        task = input("enter the task: ")
        target = input("enter the target")
        pp = "TASK" +str(i)+' :'
        qq = "TARGET" +str(i)+' :'

        f1.write(pp)
        f1.write(task)
        f1.write("\n")
        f1.write(qq)
        f1.write(target)
        f1.write("\n")

        print("Do you want to stop press space bar otherwise enter")
        s = input()
        if s == ' ':
            break
    f1.close()
def task_update(username):
    username = username+" TASK.txt"
    print("Please enter the tasks that are completed")
    task_completed = input()
    print("Enter task which are still not started by you")
    task_not_started = input()
    print("Enter task which you are doing")
    task_ongoing = input()

    fw = open(username, 'a')
    DT = str(datetime.datetime.now())

    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASKS: ")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASKS: ")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED: ")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    ussnm = username + " TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()

def signup() :
    print("Please enter the username by which you wanna access your account")
    username = input("please enter here: ")
    password = input("Enter a password: ")
    user_information(username,password)
    print("Proceed to login... ")
    login()

if __name__ == '__main__':
    print("WELCOME TO YOUR CONSOLE TASK MANAGER")
    a = int(input("If you are new to this software, please press 1. Otherwise please press 0:: "))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("WRONG INPUT! TRY AGAIN.")
