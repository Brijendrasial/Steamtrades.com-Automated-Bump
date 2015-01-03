import os

path = os.path.dirname(__file__)
try:
    os.makedirs(path+'output')
    os.makedirs(path+'data')
except OSError,e:
    pass
 

def chk_min(no):

    if no >= 2100:
        return True
    else:
        return False

def chk_value(no1,no2):
    if no2 > no1:
        return True
    else:
        return False



def enter_sleep_time():
    input_time = raw_input('\nEnter the sleep time range(Default is 2100-2600)\nPress ENTER for default\n')

    if input_time is '':
        f = open(path+'data/sleep_time.txt', 'w')
        time_range = '2100-2600'
        f.write(time_range)
        print('\nDefault time 35-40 min set\n')
   
    else:
        try:
            time1,time2 = input_time.split('-')
            time1 = int(time1)
            time2 = int(time2)

            if chk_value(time1,time2) and chk_min(time1) is True:
                f = open(path+'data/sleep_time.txt', 'w')
                f.write(input_time)
                print "\nNew sleep time range is %s\n"%input_time
            else:
                print "\nERROR: Wrong input (start range cannot be less than 2100)\n"
                enter_sleep_time()



                
        except ValueError, e:
            print '\nError: Wrong Input\n'
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
    f.write(url+'\n')
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
            print '\nThis setting is for sleep time range'
            print '\neg if range in 2100-2600(dafault) program will stop for any time between 2100-2600'
            enter_sleep_time()
        elif no is '4':
            exit()
        
        else:
            print'\n Wrong input \n'

    except NameError, e:
        exit()
    
        
