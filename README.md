Steamtrades.com-Automated-Bump
==============================

Automated Bump Threads in steamtrades.com

My steam URL: https://steamcommunity.com/id/aaj-blue-hai-paani/

This script will automatically bump your thread after particular time specified by user. Default time set in script is 35 minutes.

NOTE: Software is in testing mode and may cause errors. Please report if you encounter any. :)

**Prerequisites:**
======================================================================================================================

1) You need to install python2.7: https://www.python.org/downloads/

2) You need to login in steamtrades.com using any browser (Chrome).

3) steamtrades.com cookie [PHPSESSID content] is needed to verify your account.


**How to Use steamtrades_settings.py:**
======================================================================================================================
Run steamtrades_settings.py
```
C:\Users\xxxx\Desktop\steamtrades>python steamtrades_settings.py

####################################################################


This script is for setting the configuration adding url & cookies

1.Enter URL
2.Enter cookie
3.Enter sleep time
4.Exit
```

Press 1. Enter your steamtrades.com thread url. (You can also enter multiple url one by one)

Press 2. Enter your steamtrades.com cookie info. (Enter the content part as shown in image below)

Press 3. Enter sleep time in seconds. (Specify after how many minutes script will auto bump)

![](http://s17.postimg.org/gccyqf2z3/Untitled.png)

======================================================================================================================

**Final Step:**
======================================================================================================================
Run steamtrades.py

```
C:\Users\xxxx\Desktop\steamtrades>python steamtrades.py

Sleep time is xxxx


Bump Started.....


Bumped http://www.steamtrades.com/forum/xxxx/thread-name 1 times
 at 2014-12-30 12:33:42
 ```

======================================================================================================================

UPDATED:
======================================================================================================================

* Auto formkey scrapper added.
* Bump time left displayed.
* PHPSESID name need not to enter.
* Bump time added in settings file.
* Output folder added to display bump output.
* Data folder added for database assignment.

