
def write_link():
    file_name = 'links_steam_trades.txt'
    print '\nEnter your thread url\n'
    url = raw_input()
    if url is '':
        print '\nNo Url entered\n'
        write_link()
    else:
        f = open('links_steam_trades.txt', 'a')
        f.write(url + '\n')
        f.close
        print'\nURL successfully saved in %s\n'%(file_name)

def write_cookies():
    print '\nEnter the new cookie name for steamtrades.com\n'
    cookie_name = raw_input()
    f = open('cookie_steam_trades.txt', 'w')
    f.write(cookie_name + '\n')
    f.close
    f = open('cookie_steam_trades.txt', 'a')
    print '\nEnter the value for %s'%cookie_name
    cookie_value = raw_input()
    f.write(cookie_value + '\n')
    f.close
    

print '\n####################################################################\n'
print '\nThis script is for setting the configuration adding url & cookies\n'
message = "1.Enter your steamtrades.com thread url\n2.Enter your steamtrades.com cookie\n3.Exit\n\n"
while  True:
    print message
    try:
        no = raw_input()
        if no is '1':
            write_link() 
        elif no is '2':
            write_cookies()

        elif no is '3':
            exit()
        else:
            print'\n Wrong input \n'

    except NameError, e:
        exit()
    
        
