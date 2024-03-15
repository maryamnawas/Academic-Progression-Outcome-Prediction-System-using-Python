progress = 0
trailer = 0
module_retriever = 0
exclude = 0
data_list = []
progression_data_dict = {}

print('Part 1:')
def credits_input(level):  #to get inputs and validation
    while True:
        try:
            credit = int(input('Enter your total ' + level + ' credits: '))
            if credit < 0 or credit > 120 or credit % 20 != 0:
                print('Out of range \n')
                continue
        except ValueError:
            print('Integer required \n')
            continue
        break
    return credit
 
def progression_for_students():  #predict progression
    while True:
        credits_pass = credits_input('pass')
        credits_defer = credits_input('defer')
        credits_fail = credits_input('fail')

        if (credits_pass + credits_defer + credits_fail) != 120:
            print('Total incorrect \n')
            continue
        break

    global progress, trailer, module_retriever, exclude
    
    if credits_pass == 120:
        progression_outcome = 'Progress'
        progress += 1
    elif credits_pass == 100:
        progression_outcome = 'Progress(module trailer)'
        trailer += 1
    elif credits_fail == 80 or credits_fail == 100 or credits_fail == 120:
        progression_outcome = 'Exclude'
        exclude += 1
    else:
        progression_outcome = 'Module retriever'
        module_retriever += 1

    #appending to list
    data_list.append([progression_outcome, credits_pass, credits_defer, credits_fail])

    data_file = open('datafile.txt', 'a')  #appending to the file datafile.txt
    data_file.write(f'{progression_outcome} = {credits_pass},{credits_defer},{credits_fail}\n')
    data_file.close()

    print(progression_outcome)

    while True:  #asking for  student ID
        student_id = input('Enter your student ID: ')
        if student_id[0] != 'w' or student_id[1:].isdigit() != True or len(student_id) != 8:
            print('Invalid student ID, please reenter correctly..')
        elif student_id in progression_data_dict.keys():
            print('The entered student ID already exists, please reenter the correct student ID!!!')
        else:
            break

    #assigning keys and values
    key = student_id
    value = progression_outcome + '-' + str(credits_pass) + ',' + str(credits_defer) + ',' + str(credits_fail)
    progression_data_dict[key] = value


def histogram(outcome, outcome_value):  #histogram
    print(f"{outcome:10} {outcome_value:5} : {'*' * outcome_value}")

while True:
    try:
        version = int(input('''
Enter 1 if you are a student:
Enter 2 if you are a staff member:
Enter 3 to stop the program:

Enter your option here: '''))

        if version == 1:
            print('Student version \n')
            progression_for_students()

        elif version == 2:
            data_file = open('datafile.txt', 'w')  #opens a file and overwrites to it
            data_file.close()
            
            print('Staff member version \n')

            while True:
                progression_for_students()
                
                valid = input('''
Would you like to enter another set of data?        
Enter 'y' for yes or 'q' to quit and view results: ''')
                if valid == "q":
                    break
                elif valid != "y" and "q":
                    print('Invalid input!! please reenter "y" or "q"\n')
                    continue
                print()

            print('-' * 64)
            print('Histogram\n')   #Histogram

            histogram('progress', progress)
            histogram('Trailer', trailer)
            histogram('Retriever', module_retriever)
            histogram('Excluded', exclude)
            print()
            print(f'{progress+trailer+module_retriever+exclude} outcomes in total.')
            print('-' * 64)

            print('Part 2: \n')  #list 
            for item in data_list:
                print(f'{item[0]} = {item[1]},{item[2]},{item[3]}')
            print()

            print('Part 3: \n')   #textfile 
            data_file = open('datafile.txt', 'r')    #reads from the saved file
            readfile = data_file.readlines()    #reads the whole file and returns a list
            for each in readfile:
                print(each,end='')
            data_file.close()  #closing the file
            print()

            print('Part 4: \n')  #dictionary          
            for (keys, values) in progression_data_dict.items():
                print(keys + ':' + values, end = ' ')
            print()
            
        elif version == 3:
            break

        else:
            print('invalid option!! please reenter...')
    
    except ValueError:
        print('Invalid option, please enter 1 or 2 or 3')
        continue
