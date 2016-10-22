import random
import time
import sqlite3



name_user = input("What is your name?: ")

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()


def print_menu():
    print('Print 1 to start questions')
    print('Print 2 to times')
    print('Print 3 to exit')


def funk():
    num_first_ran = random.randint(0, 20)
    num_second_ran = random.randint(0, 20)
    sum_num = num_first_ran + num_second_ran
    min_num = num_first_ran - num_second_ran

    def ran_num():
        if num_first_ran > num_second_ran:
            quest = int(input("what's: {} - {} = ".format(num_first_ran, num_second_ran)))
            if quest == min_num:
                print("Well done")
            else:
                print("Again please")
                ran_num()
        elif num_first_ran < num_second_ran:
            quest = int(input("what's: {} + {} = ".format(num_first_ran, num_second_ran)))
            if quest == sum_num:
                print("Well done")
            else:
                print("Again please")
                ran_num()
    ran_num()

def cteate_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT, time1 REAL)")



def menu():
    name_user
    cteate_table()
    print_menu()
    item = input('Choose menu item.')
    if item == '1':
        start_time = int(time.time())
        for i in range(2):
            funk()
        end_time = int(time.time())
        time1 = end_time - start_time
        print(time1)
        def data_entry():
            c.execute("INSERT INTO stuffToPlot VALUES({},{})".format(name_user, time1))
            conn.commit()
            c.close()
            conn.close()
        data_entry()
    elif item == '2':
        c.execute("SELECT * FROM stuffToPlot")
        print (c.fetchall())
    elif item == '3':
        return
    else:
        print('Choose right menu item.')
        menu()

menu()



