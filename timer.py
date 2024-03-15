import time
import os
import csv
from datetime import datetime, date, timedelta

FILE_NAME = 'log.csv'

def stopwatch_timer():
    start_time = time.time()
    time_str = str()
    start_date_time = datetime.now().replace(microsecond=0)

    try:
        while True:
            current_time = time.gmtime(time.time() - start_time)
            time_str = time.strftime("%M minutes, %S seconds", current_time)
            print(time_str, end="\r")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nTimer stopped!")

    finish_date_time = datetime.now().replace(microsecond=0)

    message = input('Enter a message: ')
    if message is '':
        message = 'Null'

    total_time = time_str.split(' ') 
    log_list = [total_time[0], total_time[2], start_date_time, finish_date_time ,message]

    with open(FILE_NAME, 'a') as log:   
        w = csv.writer(log)
        w.writerow(log_list)


def countdown_timer(minutes):
    total_time = [str(minutes), "00"]
    total_seconds = minutes * 60
    time_str = str()
    start_date_time = datetime.now().replace(microsecond=0)

    try:
        for i in range(total_seconds, 0, -1):
            time_str = f"Time remaining: {i // 60} minutes {i % 60} seconds"
            print(time_str, end="\r")
            time.sleep(1)

    except KeyboardInterrupt:
        temp = time_str.split(' ')
        total_time = total_seconds - (int(temp[2]) * 60 + int(temp[4]))
        total_time = [str(total_time // 60) , str(total_time % 60)] 
    
    finish_date_time = datetime.now().replace(microsecond=0)
    
    message = input('\n\nEnter a message: ')
    if message is '':
        message = 'Null'
    
    log_list = [total_time[0], total_time[1], start_date_time, finish_date_time ,message]
    
    with open(FILE_NAME, 'a') as log:   
        w = csv.writer(log)
        w.writerow(log_list)


def time_conversion(total_time):
    hour = total_time // 3600
    minutes = (total_time % 3600) // 60
    second = total_time % 60
    print(f'{hour}:{minutes}:{second}')


def specific_day_time(day):
    print(day)
    total_time = 0
    with open(FILE_NAME, 'r') as log:
        r = csv.reader(log)
        for i in r:
            date_csv, _ = i[2].split(' ')
            if  day == date_csv:
                total_time += int(i[0]) * 60 + int(i[1]) 

        time_conversion(total_time=total_time)
        print()


def main():

    os.system('clear')
    option = int()

    while(True):
        print('1) start timer')
        print('2) count down')
        print('3) total times today')
        print('4) total times last week')
        print('5) total time last month')
        print('6) exit')

        print('\n-----------------------------------\n')
       
        while(True):
            try:
                option = int(input('choose an option: '))
                break
            
            except: 
                print('please enter valid input ')
                continue

        if(option == 1):
            os.system('clear')

            print('timer started!')
            print("Press Ctrl+C to stop the timer.\n\n")
            stopwatch_timer()

            os.system('clear')
   
        elif(option == 2):
            count_down = int()

            os.system('clear')
            
            while(True):
                try:
                    count_down = int(input("Enter a time in minutes for the countdown: "))
                    break
                except:
                    print('please enter valid input ')
                    continue

            countdown_timer(count_down)

            os.system('clear')

        elif(option == 3):
            os.system('clear')
                
            today = str(date.today())                
            specific_day_time(today)

            input("\nEnter space to continue...")

            os.system('clear')
        
        elif(option == 4):
            os.system('clear')

            today = date.today()
            week_list = list()
            total_time = 0

            for i in range(0,7):
                day = str(today - timedelta(days=i))
                specific_day_time(day)
                week_list.append(day)

            with open(FILE_NAME, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    date_csv, _ = i[2].split(' ')
                    if date_csv in week_list:
                        total_time += int(i[0]) * 60 + int(i[1])
                
                print('totla time: ', end='')
                time_conversion(total_time=total_time)
            
            input("\nEnter space to continue...")

            os.system('clear')
        
        elif(option == 5):
            os.system('clear')

            total_time = 0

            with open(FILE_NAME, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    total_time += int(i[0]) * 60 + int(i[1])
                
                print('totla time: ', end='')
                time_conversion(total_time=total_time)
            
            input("\nEnter space to continue...")

            os.system('clear')

        elif(option == 6):
            os.system('clear')
            break;



if __name__ == "__main__":
    main()