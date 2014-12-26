Steamtrades.com-Automated-Bump
==============================

Automated Bump Threads in steamtrades.com

My steam URL: https://steamcommunity.com/id/aaj-blue-hai-paani/

This script will automatically bump your thread after particular time specified by user. Default time set in script is 35 minutes.

NOTE: Software is in testing mode and may cause errors. Please report if you encounter any. :)

**Prerequisites:**

1) You need to install python: https://www.python.org/downloads/

2) Python request module is needed: https://pypi.python.org/pypi/requests

3) You need to login in steamtrades.com using any browser (Chrome).

4) steamtrades.com cookie [PHPSESSID Value] is needed to verify your account.

5) form_key value is needed to authorise your post.


**How to Use steamtrades_settings.py:**
======================================================================================================================
Run steamtrades_settings.py
```
python steamtrades_settings.py

####################################################################


This script is for setting the configuration adding url & cookies

1.Enter your steamtrades.com thread url
2.Enter your steamtrades.com cookie
3.Exit
```

Press 1 and enter your steamtrade.com thread url. You can enter multiple urls also.

Press 2 to enter your cookie info.

It will ask for "Enter the new cookie name for steamtrades.com". Input "PHPSESSID" without quotes and press enter.
It will then ask for "Enter the value for PHPSESSID". Input Value of "Content" and press enter.

![](http://s17.postimg.org/gccyqf2z3/Untitled.png)

======================================================================================================================

**How to Use steamtrades.py:**
======================================================================================================================
Open your steamtrades.com thread url and view source of the page. Search for the code below and Copy the value="xxxxxxxxxxxxxxxxxxxx" as defined. We need to copy xxxxxxxxxxxxx and save it to notepad file.

```
</form><form id="bump_discussion" action="" method="post"><input type="hidden" name="form_key" value="xxxxxxxxxxxxxxxxxxxx" /><input type="hidden" name="do" value="bump" /></form>	
```

Now open steamtrades.py using a text editor and look for the line 38. It should be like below:

```
payload = {'form_key':'9ebde2e0527708a29d2889708d0a3bc7', 
```

Just Copy 'xxxxxxx' part which you saved in text file and replace '9ebde2e0527708a29d2889708d0a3bc7' with that.

======================================================================================================================

**Final Step:**
======================================================================================================================
Run steamtrades.py and provide after how many seconds you want to bump a thread (Default is 35 minutes i.e 2100 seconds). It will automatically bump thread after specified time.

======================================================================================================================

**Note: This is initial release and we will provide more updation very soon to simply wole process.**


