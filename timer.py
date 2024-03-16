import time
import os
import csv
from datetime import datetime, date, timedelta
import glob

FILE_NAME = 'log.csv'


def stopwatch_timer() -> None:

    print('timer started!')
    print("Press Ctrl+C to stop the timer.\n\n")

    start_time = time.time()
    start_date_time = datetime.now().replace(microsecond=0)
    time_str = str()
    
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


def countdown_timer(minutes) -> None:

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


def time_conversion(total_time_second):
    hour = total_time_second // 3600
    minutes = (total_time_second % 3600) // 60
    second = total_time_second % 60
    print(f'{hour}:{minutes}:{second}')


def specific_day_time(day):
    print(day)
    total_time_second = 0
    with open(FILE_NAME, 'r') as log:
        r = csv.reader(log)
        for i in r:
            date_csv, _ = i[2].split(' ')
            if  day == date_csv:
                total_time_second += int(i[0]) * 60 + int(i[1]) 
    time_conversion(total_time_second=total_time_second)
    print()
    return total_time_second


def main():

    os.system('clear')
    option = int()

    while(True):
        print('1) start timer')
        print('2) count down')
        print('3) total times today')
        print('4) total times last week')
        print('5) total time in this file')
        print('6) total time in selected file')
        print('7) exit')

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
            stopwatch_timer()
            os.system('clear')
   
        elif(option == 2):
            os.system('clear')

            count_down = int()            
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

            _ = specific_day_time(str(date.today()))
            input("Enter space to continue...")

            os.system('clear')
        
        elif(option == 4):
            os.system('clear')

            today = date.today()
            total_time_second = 0

            for i in range(0,7):
                day = str(today - timedelta(days=i))
                total_time_second += specific_day_time(day)

            print('total time: ', end='')
            time_conversion(total_time_second=total_time_second)
            
            input("\nEnter space to continue...")

            os.system('clear')
        
        elif(option == 5):
            os.system('clear')

            total_time_second = 0

            with open(FILE_NAME, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    total_time_second += int(i[0]) * 60 + int(i[1])
                
            print(f'totla time in {FILE_NAME.rstrip('.csv')}: ', end='')
            time_conversion(total_time_second=total_time_second)
            
            input("\nEnter space to continue...")

            os.system('clear')
        
        elif(option == 6):
            os.system('clear')

            csv_list = glob.glob("*.csv")
            
            for i in csv_list:
                print(f'{csv_list.index(i) + 1}.{i}')
            
            while(True):
                try:
                    selected_index = int(input('\n\nplease choose a csv file to show total time: '))
                    file_name = csv_list[selected_index - 1]
                    break
                except:
                    print('please enter valid input!')
                    continue

            os.system('clear')

            total_time_second = 0

            with open(file_name, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    total_time_second += int(i[0]) * 60 + int(i[1])
                
                print(f'totla time in {file_name.rstrip('.csv')}: ', end='')
                time_conversion(total_time_second=total_time_second)

            input("\nEnter space to continue...")

            os.system('clear')
        
        elif(option == 7):
            os.system('clear')
            break;



if __name__ == "__main__":
    main()