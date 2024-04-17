import time
import os
import csv
from datetime import datetime, date, timedelta
import glob
import pyfiglet
from colorama import Fore, Back, Style

FILE_NAME = 'test.csv'


def stopwatch_timer() -> None:

    print(Fore.GREEN + 'timer started!' + Style.RESET_ALL)
    print(Fore.CYAN + 'Press Ctrl+C to stop the timer.' + Style.RESET_ALL + '\n\n')

    start_time = time.time()
    start_date_time = datetime.now().replace(microsecond=0)
    time_str = str()
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            time_str = f"{minutes:02d} {Fore.BLUE}minutes{Style.RESET_ALL}, {seconds:02d} {Fore.BLUE}seconds{Style.RESET_ALL}"
            print(time_str, end="\r")
            time.sleep(1)
            
            if minutes >= 60:
                print("\n\n" + Fore.YELLOW + "Timer reset to zero!" + Style.RESET_ALL)
                start_time = time.time()

    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "Timer stopped!" + Style.RESET_ALL)

    finish_date_time = datetime.now().replace(microsecond=0)

    message = input(Fore.YELLOW + 'Enter a message: ' + Style.RESET_ALL)
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

    print()

    try:
        for i in range(total_seconds, 0, -1):
            time_str = Fore.CYAN + "Time remaining: " + Style.RESET_ALL + f' {i // 60} minutes {i % 60} seconds'
            print(time_str, end="\r")
            time.sleep(1)
        os.system('make; spd-say \'pashoo pashoo tamom shoad\'')

    except KeyboardInterrupt:
        temp = time_str.split(' ')
        total_time = total_seconds - (int(temp[3]) * 60 + int(temp[5]))
        total_time = [str(total_time // 60) , str(total_time % 60)]
        print("\n\n" + Fore.RED + "Timer stopped!" + Style.RESET_ALL) 
    
    finish_date_time = datetime.now().replace(microsecond=0)
    
    message = input(Fore.YELLOW + 'Enter a message: ' + Style.RESET_ALL)
    if message is '':
        message = 'Null'
    
    log_list = [total_time[0], total_time[1], start_date_time, finish_date_time ,message]
    
    with open(FILE_NAME, 'a') as log:   
        w = csv.writer(log)
        w.writerow(log_list)


def time_conversion(total_time_second, color='GREEN'):
    hour = total_time_second // 3600
    minutes = (total_time_second % 3600) // 60
    second = total_time_second % 60
    
    if(color == 'GREEN'):
        print(Fore.GREEN + f'{hour}:{minutes}:{second}' + Style.RESET_ALL)
    
    elif(color == 'WHITE'):
        print(Fore.WHITE + f'{hour}:{minutes}:{second}' + Style.RESET_ALL)


def specific_day_time(day):
    print(Fore.BLUE + day + Style.RESET_ALL)
    total_time_second = 0
    with open(FILE_NAME, 'r') as log:
        r = csv.reader(log)
        for i in r:
            date_csv, _ = i[2].split(' ')
            if  day == date_csv:
                total_time_second += int(i[0]) * 60 + int(i[1]) 
    time_conversion(total_time_second=total_time_second)
    return total_time_second


def main():

    os.system('clear')

    option = int()

    while(True):
        title_text = pyfiglet.figlet_format('amir timer', font='slant')        
        print(Back.BLACK + Fore.YELLOW + Style.BRIGHT + title_text + Style.RESET_ALL)
        
        print(Fore.CYAN + '1: ' + Style.RESET_ALL + 'start timer')
        print(Fore.CYAN + '2: ' + Style.RESET_ALL + 'count down')
        print(Fore.CYAN + '3: ' + Style.RESET_ALL + 'total times today')
        print(Fore.CYAN + '4: ' + Style.RESET_ALL +  'total times last week')
        print(Fore.CYAN + '5: ' + Style.RESET_ALL +  'total time in this file')
        print(Fore.CYAN + '6: ' + Style.RESET_ALL +  'total time in selected file')
        print(Fore.CYAN + '7: ' + Style.RESET_ALL +  'exit')

        print('\n-----------------------------------\n')
       
        while(True):
            try:
                option = int(input(Fore.GREEN    + 'choose an option: ' + Style.RESET_ALL))
                break
            
            except: 
                print(Fore.RED + 'please enter valid input' + Style.RESET_ALL)
                print()
                continue

        if(option == 1):
            os.system('clear')
            
            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.WHITE + Style.BRIGHT + title_text + Style.RESET_ALL)
            
            stopwatch_timer()
            
            os.system('clear')
   
        elif(option == 2):
            os.system('clear')
            
            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.BLUE + Style.BRIGHT + title_text + Style.RESET_ALL)
            
            count_down = int()            
            while(True):
                try:
                    count_down = int(input(Fore.GREEN + "Enter a time in minutes for the countdown: " + Style.RESET_ALL))
                    break
                
                except:
                    print(Fore.RED + 'please enter valid input ' + Style.RESET_ALL)
                    print()
                    continue
                
            countdown_timer(count_down)

            os.system('clear')

        elif(option == 3):
            os.system('clear')

            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.RED + Style.BRIGHT + title_text + Style.RESET_ALL)
            
            _ = specific_day_time(str(date.today()))
            print()
            input(Fore.YELLOW + "Enter space to continue..." + Style.RESET_ALL)

            os.system('clear')
        
        elif(option == 4):
            os.system('clear')

            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.CYAN + Style.BRIGHT + title_text + Style.RESET_ALL)

            today = date.today()
            total_time_second = 0

            for i in range(0,7):
                day = str(today - timedelta(days=i))
                total_time_second += specific_day_time(day)
                print('------------')

            print()
            print(Fore.CYAN + 'total time: ' + Style.RESET_ALL, end='')
            time_conversion(total_time_second=total_time_second, color='WHITE')
            
            input("\n" + Fore.YELLOW + "Enter space to continue..." + Style.RESET_ALL)

            os.system('clear')
        
        elif(option == 5):
            os.system('clear')
            
            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.GREEN + Style.BRIGHT + title_text + Style.RESET_ALL)
            
            total_time_second = 0

            with open(FILE_NAME, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    total_time_second += int(i[0]) * 60 + int(i[1])
                
            print(Fore.CYAN + f'totla time in {FILE_NAME.rstrip('.csv')}: ' + Style.RESET_ALL, end='')
            time_conversion(total_time_second=total_time_second, color="WHITE")
            
            input("\n" + Fore.YELLOW + "Enter space to continue..." + Style.RESET_ALL)

            os.system('clear')
        
        elif(option == 6):
            os.system('clear')

            title_text = pyfiglet.figlet_format('amir timer', font='slant')        
            print(Back.BLACK + Fore.BLUE + Style.BRIGHT + title_text + Style.RESET_ALL)

            csv_list = glob.glob("*.csv")
            csv_list.sort()
            
            for i in csv_list:
                print(Fore.CYAN + f'{csv_list.index(i) + 1}:' + Style.RESET_ALL + f'{i}')
            
            is_breake = 0
            while(True):
                try:
                    selected_index = int(input('\n\n' + Fore.WHITE + 'please choose a csv file to show total time: ' + Style.RESET_ALL))
                    if(selected_index == 0):
                        is_breake = 1
                        break
                    file_name = csv_list[selected_index - 1]
                    break
                except:
                    print(Fore.RED + 'please enter valid input!' + Style.RESET_ALL)
                    continue

            os.system('clear')

            if(is_breake == 1):
                continue
            
            total_time_second = 0

            with open(file_name, 'r') as log:
                r = csv.reader(log) 

                for i in r:
                    total_time_second += int(i[0]) * 60 + int(i[1])
                
                print(Fore.BLUE + f'totla time in' + Style.RESET_ALL + Fore.CYAN + f' {file_name.rstrip('.csv')}: ' + Style.RESET_ALL, end='')
                time_conversion(total_time_second=total_time_second)

            input("\n" + Fore.YELLOW + "Enter space to continue..." + Style.RESET_ALL)

            os.system('clear')
        
        elif(option == 7):
            os.system('clear')
            break;



if __name__ == "__main__":
    main()