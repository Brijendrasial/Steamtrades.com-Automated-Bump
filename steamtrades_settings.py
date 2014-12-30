import os

path = os.path.dirname(__file__)
try:
    os.makedirs(path+'output')
    os.makedirs(path+'data')
except OSError,e:
    pass
 
def enter_sleep_time():
    input_time = raw_input('\nEnter the sleep time\n')

    if input_time is '':
        print('\nERROR: Time cannot be black\n')
        enter_sleep_time()
   
    else:
        try:
            input_time = int(input_time)
            if input_time < 2100:
                print '\nERROR: Time can not be less than 2100 sec\n'
                enter_sleep_time()
            else:
                f = open(path+'data/sleep_time.txt', 'w')
                f.write(input_time)
                print '\nYour new sleep time is %s\n'%input_time
                
                
        except ValueError, e:
            print '\n Enter integer value\n'
            enter_sleep_time()
            
        
def enter_cookies():
    cookie = raw_input('\nEnter the cookie\n')
    f = open(path+'data/cookie_steam_trades.txt', 'w')
    f.write(cookie)
    f.close()
    print ('\n cookies %s Successfully entered\n'%cookie)
    
       
def enter_url():
    url = raw_input('\nEnter the url\n')
    f = open(path+'data/links_steam_trades.txt', 'a')
    f.write(url)
    f.close()
    print ('\n Url %s Successfully entered\n'%url)
    


print '\n####################################################################\n'
print '\nThis script is for setting the configuration adding url & cookies\n'
message = "1.Enter URL\n2.Enter cookie\n3.Enter sleep time\n4.Exit\n\n"
while  True:
    print message
    try:
        no = raw_input()
        if no is '1':      
            enter_url()
            
        elif no is '2':
            enter_cookies()

        elif no is '3':
            enter_sleep_time()
        elif no is '4':
            exit()
        
        else:
            print'\n Wrong input \n'

    except NameError, e:
        exit()
    
        
