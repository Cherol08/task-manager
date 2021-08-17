from datetime import date, datetime

# This program is created to store details of various users, their tasks, statistics and allow them to access their own
# or collective info of other users as well.
# Imported the datetime module to be able to use date and datetime to store deadliness in appropriate date format.
# 'user' will store list of usernames and a passwords and check if what the user enters in the list then confirm login.

username = input("\nEnter your username: ")
password = input("Enter your password: ")

login = True
admin = False
users = ""

#  Opened the file with usernames and added them to the empty string, converted to a list. If username is in
# in the list of user's access will b granted.

with open('user.txt', 'r') as user_file:
    users += user_file.read()
    users = users.split()

    while username and password not in users:
        login = False
        print("\nInvalid details. Please enter  correct details!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username and password in users:
            login = True


# reg_user() used to registered new user's. It checks whether user entered an existing name.
# If so, will be prompted to enter new name until they choose one which doesnt already exist. Function also checks
# user's password, tasking the correct details and adding them to the file containing names of user's.


def reg_user(name):
    new_user = ""

    with open('user.txt', 'r+') as users_file:
        for a_line in users_file:
            a_line = a_line.rstrip()
            a_line = a_line.split(",")
            new_user += str(a_line[0]) + ","  # program will add each line it reads to the string 'user'

        while name in new_user:
            print("\nUsername already exists.")
            name = input("Enter different username: ")
            if name not in new_user:
                continue

        pass_word = input("Enter password: ")
        right_password = input("Confirm password: ")

        while pass_word != right_password:
            print("\nIncorrect Details.Please try again.")
            pass_word = input("Enter password: ")
            right_password = input("Confirm password: ")
            if pass_word == right_password:
                continue

    login_details = "{}, {} ".format(name, pass_word)

    with open('user.txt', 'a+') as u_file:
        u_file.read()
        u_file.write("\n" + login_details)

    print("\nUser successfully registered!")


# format_data() puts user task info in a user-friendly format.

def format_data(task_title, user_name, date_assigned, date_due, complete, task_type):
    user_data = ("\nTask:\t\t\t{}\nAssigned to:\t\t{}\nDate assigned:\t\t{}\nDate due:\t\t{}\nTask complete:\t"
                 "\t{}\nTask description:\t{}".format(task_title, user_name, date_assigned, date_due, complete,
                                                      task_type))
    return user_data


# add_task() adds new tasks to tasks file when called. It allows user to enter details about the new task and
# the adds them to the file.


def add_task():
    new_user = input("\nEnter username to assign task: ")
    task = input("Enter task: ").capitalize()
    task_description = input("Enter task description ").capitalize()
    task_due_date = input("Enter date task is due(DD Mon YYYY): ").title()
    assign_date = (datetime.today().strftime('%d %b %Y')).title()
    task_done = "No"

    # new_data formats input correctly before it is added the to the task file.
    new_data = (
        "{}, {}, {}, {}, {}, {}".format(new_user, task, task_description, assign_date, task_due_date, task_done))

    with open('tasks.txt', 'a+') as task_file:
        task_file.read()
        task_file.write("\n" + new_data)

    print("\nTask successfully added!")


# view_all() function opens task file and displays all the tasks in the file using the format_data()
# function to display it in a friendly manner.


def view_all():
    with open('tasks.txt', 'r') as task_file:
        for a_line in task_file:
            a_line = a_line.rstrip()
            a_line = a_line.split(", ")

            all_tasks = format_data(a_line[1], a_line[0], a_line[3], a_line[4], a_line[5], a_line[2])
            print(all_tasks + "\n")


# view_mine() function opens task file and users task_num to count and retrieve only the tasks assigned
# to the user logged in. Also displays them using the format_data function.


def view_mine():
    task_num = 0

    with open('tasks.txt', 'r') as task_file:
        for a_line in task_file:
            a_line = a_line.rstrip()
            a_line = a_line.split(", ")

            if a_line[0] == username:  # this checks the names in the file, if they match the user's
                task_num += 1
                mine = format_data(a_line[1], a_line[0], a_line[3], a_line[4], a_line[5], a_line[2])
                print(f"\nTask{task_num}:\n{mine}")


# integer_date() function coverts inputted date from string to integer.
# The due date of the tasks were indexed, converted to datetime objects and the format changed from string to
# numbers(Samuel, 2018).


def integer_date(date_input):

    date_input = datetime.strptime(date_input, '%d %b %Y')
    num_format = datetime.strftime(date_input, '%d %m %Y')  # turning date into numbers

    # date() stores dates as integer values which allows us to use assignment operators to compare which
    # dates are older to get deadlines, (louse, 2020).

    num_format = num_format.split(" ")
    num_format = [int(i) for i in num_format]
    due_date = date(num_format[2], num_format[1], num_format[0])
    return due_date


if login:

    print("\nLogin Successful.")

    while True:

        if username == "admin":
            admin = True
            admin_menu = '''\nPlease select one of the following options:\nr - register user\na - add a task\
            \nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit'''
            print(admin_menu)
        else:
            user_menu = '''\nPlease select one of the following options:\nr - register user\na - add a task\
            \nva - view all tasks\nvm - view my tasks\ngr - generate reports\ne - exit'''
            print(user_menu)

        option = input("\nEnter option: ").lower()

        # if user chooses option 'r', he'll be asked for the details of the new user they want to register,
        # and reg_user() function is called.

        if option == "r" and admin:
            new_name = input("\nEnter new user's username: ")
            reg_user(new_name)
            break

        # if user chooses to 'r' and is not admin an error message will be displayed and user will have to pick
        # a different option.

        elif option == "r" and not admin:
            print("\nUnsuccessful attempt.\nOnly authorised users can register new users.")

        # add_task() function is called if user chooses to add new task
        elif option == 'a':
            add_task()
            break

        # view_all() function is called if user chooses to view all tasks
        elif option == "va":
            view_all()
            break

        # view_mine() function is called if user chooses to view all their tasks
        # User can choose to edit tasks by selecting which task they want to edit and what they want to edit
        # about the task.

        elif option == "vm":
            view_mine()

            print("\nSelect option:\n 1 - choose specific task\n-1 - return to main menu")
            next_option = int(input("\n Enter number: "))

            if next_option == 1:

                task2_edit = int(input("Enter task number to edit: "))
                print("\nSelect option:\na - Mark as complete\nb - edit task")
                action = input("select option: ").lower()

                # Boolean will help check task completion and counters check which lines in file contain user's
                # tasks and also count them. empty string will append the lines as strings  so they can be updated
                # when changes are made.

                task_completion = False
                line_count = 0
                task_count = 0
                str_lines = ""

                with open('tasks.txt', 'r') as user_tasks:
                    if action == 'a':
                        for line in user_tasks:
                            line_count += 1
                            line = line.rstrip()
                            line = line.split(", ")

                            if line[0] == username:  # checks if tasks belongs to user.
                                task_count += 1
                                if task_count == task2_edit:
                                    line[5] = "Yes"  # marks task as complete
                                    print("\nTask complete!")

                            str_lines += str(", ".join(line)) + "\n"

                    # if user chooses to edit task, he will choose between changing the user task is assigned to or the
                    #  deadline of the task.

                    elif action == 'b':
                        for line in user_tasks:
                            line_count += 1
                            line = line.rstrip()
                            line = line.split(", ")

                            # If task is already complete user will not be able to make changes.
                            if line[5] == "Yes" and line[0] == username:
                                task_completion = True
                                print("\nTask is already complete!")
                                break

                            #  ask_count count's the tasks in the file that belong to user.
                            if line[0] == username:
                                task_count += 1
                                if task_count == task2_edit:
                                    change = input("Edit username or deadline? ").lower()

                                    if change == "username":
                                        username_4task = input("username to assign task: ")
                                        line[0] = username_4task
                                    elif change == "deadline":
                                        new_deadline = input("Enter new deadline (DD Mon YYYY): ")
                                        line[4] = " " + new_deadline
                                    print("\nTask edit complete!\n")

                            str_lines += str(", ".join(line)) + "\n"
                    else:
                        print("Invalid option.")
                        break

                    # If changes were made,the updated information will be added to the file.
                    if not task_completion:
                        with open('tasks.txt', 'w') as write_tasks:
                            write_tasks.write(str_lines)
                        break
                    else:
                        break

            # If user chooses to go to main menu, using continue, main menu will be displayed again
            # since the main code block is placed under a true while loop.

            elif next_option == -1:
                continue

            # if user chooses neither to edit tasks or return to main menu the error message will be displayed
            # and program will end.

            else:
                print("Invalid option.")
                break

        # if user chooses to generate reports, two files will be created containing the overall stats of users
        # and their tasks.

        elif option == "gr":
            # Opened the tasks file to obtain info for the stats from it. Counters, count how many tasks there are
            # and how many are complete, incomplete or due.

            current_date = date.today()  # variable stores today's date so it can be compared to the deadlines.
            with open('tasks.txt', 'r') as user_tasks:
                tasks = 0
                total_complete = 0
                total_incomplete = 0
                total_due = 0
                incomplete_and_due = 0

                # integer_date function is called, taking the indexed date as an argument and returning it
                # in an integer number format. if due date is older than current date it means the tasks is overdue.

                for task_line in user_tasks:
                    tasks += 1
                    task_line = task_line.rstrip()
                    task_line = task_line.split(", ")
                    date_ = integer_date(task_line[4])

                    if current_date > date_:
                        total_due += 1
                    if task_line[5] == "Yes":
                        total_complete += 1
                    if task_line[5] == "No":
                        total_incomplete += 1
                    if task_line[5] == "No" and current_date > date_:
                        incomplete_and_due += 1

                # The counters are used to calculate percentages. The overall statistics is stored
                # in the job_stats string in an easy to read format and written to a new file.

                incomplete_percentage = round((total_incomplete / tasks) * 100)
                percentage_due = round((total_due / tasks) * 100)

                job_stats = f"\nTask statistics\n" \
                            f"\nTotal number of tasks: {tasks}" \
                            f"\nTotal number of complete tasks: {total_complete}" \
                            f"\nTotal number of incomplete tasks: {total_incomplete}" \
                            f"\nTotal number of incomplete and due tasks: {incomplete_and_due}" \
                            f"\nPercentage of incomplete tasks: {incomplete_percentage}%" \
                            f"\nPercentage of overdue tasks: {percentage_due}%"

                with open('task_overview.txt', 'w+') as task_overview:
                    task_overview.read()
                    task_overview.write(job_stats)

            # The stats for each specific user is also generated. all_user counts number of user's in the users file.

            with open('user.txt', 'r') as usernames_file:
                all_users = 0
                for line in usernames_file:
                    all_users += 1
                    line = line.rstrip()
                    line = line.split(", ")

                    # The if conditions apply for each user. Counters check if they have a task in the task file,
                    # how many tasks there are per user and how many are complete, incomplete or due.

                    with open('tasks.txt', 'r') as user_tasks:
                        task_per_user = 0
                        user_completed = 0
                        user_incomplete = 0
                        user_incomplete_and_due = 0

                        for task_line in user_tasks:
                            task_line = task_line.rstrip()
                            task_line = task_line.split(", ")
                            date_ = integer_date(task_line[4])

                            if line[0] == task_line[0]:
                                task_per_user += 1
                            if line[0] == task_line[0] and task_line[5] == "Yes":
                                user_completed += 1
                            if line[0] == task_line[0] and task_line[5] == "No":
                                user_incomplete += 1
                                if current_date > date_:
                                    user_incomplete_and_due += 1
                            else:
                                continue

                    # If registered user has no tasks program will continue on, else stats on their tasks will be
                    # obtained using the counters.

                    if task_per_user == 0:
                        continue
                    else:
                        percentage_user_completed = round((user_completed / task_per_user) * 100)
                        percentage_incomplete = round((user_incomplete / task_per_user) * 100)
                        percentage_tasks_per_user = round((task_per_user / tasks) * 100)
                        percentage_incomplete_due = round((user_incomplete_and_due / task_per_user) * 100)

                        user_stats = f"\nUsername: {line[0]}" \
                                     f"\nPercentage of assigned tasks: {percentage_tasks_per_user}%" \
                                     f"\nPercentage of complete tasks: {percentage_user_completed}%" \
                                     f"\nPercentage of incomplete tasks: {percentage_incomplete}%" \
                                     f"\nPercentage of incomplete and due tasks: {percentage_incomplete_due}%"

                        # once all stats are generated, they will be written to a new file

                        with open('user_overview.txt', 'a+') as user_overview:
                            user_overview.read()
                            user_overview.write("\n" + user_stats)
            break

        # if user is admin  and chooses to display the statistics. They will be obtained from the newly generated
        # files (if already created) and displayed to the in the same user-friendly format in which they are stored.

        elif option == "ds" and admin:
            str_task_report = ""
            str_user_stats = ""

            with open('task_overview.txt', 'r') as task_overview:
                str_task_report += task_overview.read()
                print(str_task_report)

            with open('user_overview.txt', 'r') as user_overview:
                str_user_stats += user_overview.read()
                print(str_user_stats)
            break

        # if user chooses to exit program will end

        elif option == "e":
            print("\nLogout Successful")
            break

        # if user chooses none of the options on the main menu, he will be prompted to choose again.

        else:
            print("\nInvalid option")
            continue

# Reference list ##########################

# Louse, L 2020, Code Grepper, Python, viewed 02 August 2021, <https://www.codegrepper.com/code-examples/python>.
# Samuel, N 2018, Stack Abuse, viewed 02 August 2021,  <https://stackabuse.com/how-to-format-dates-in-python>.
