---
title: "Selenium script to reset a ZyXEL NBG4115 4G Router"
date: 2012-04-26
---

The [ZyXEL NBG4115](http://www.steg-electronics.ch/fr/article/zyxel-nbg4115-184952.aspx?doprint=yes) is a small, cheap 3G router that can be used to build a wireless network where there is no access point available. You plug one of those 3G dongles into it, enter the PIN number, and you have a local access point in the middle of nowhere. At [Neurobat](http://neurobat.net) we use these devices whenever we require internet access to a test site that cannot have internet access otherwise. \[caption id="attachment\_604" align="alignnone" width="287" caption="ZyXEL NBG4115 Wireless N-lite 3G Router"\]\[![](images/ZY_NBG4115_2524_F72-287x300.jpg "ZyXEL NBG4115 Wireless N-lite 3G Router")\][3](http://computersandbuildings.com/wp-content/uploads/2012/04/ZY_NBG4115_2524_F72.jpg)\[/caption\] One problem we ran into very early on, however, is that the 3G connection provided by Swisscom tends to be, to put it charitably, flaky. Indeed, we have never had a single connection remain alive for more than a week. We have spoken with their tech support, upgraded the firmware on the 3G dongles, all to no avail. As a final solution we decided to write scripts on the local netbooks that would regularly (say, once every three hours) reset the connection through the router's administrative web interface. Only problem was that none of the "easy" screen-scraping tools out there (`wget`, Python's `urllib`, etc) was Javascript-capable---|which is something the web interface would detect, and refuse any client that was not Javascript-enabled. \[caption id="attachment\_605" align="alignnone" width="300" caption="3G Router on a test site"\]\[![](images/IMG_6575-300x200.jpg "3G Router on a test site")\][4](http://computersandbuildings.com/wp-content/uploads/2012/04/IMG_6575.jpg)\[/caption\] In the end we decided to install a [Selenium](http://seleniumhq.org/) server on each netbook, and wrote a Python script that would talk to the Selenium server and reset the router. If this can help anyone, here is the (simple) Python script to reset a ZyXEL 3G router through Selenium, assuming a Selenium server has been started and is listening on port 4444:

```
#!/usr/bin/env python 
from selenium import webdriver 
browser = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT) 
# Login 
browser.get("http://192.168.1.1") 
pass_field = browser.find_element_by_name("textfield") 
pass_field.clear() 
pass_field.send_keys("*****") 
pass_field.submit() 
# Click restart 
try: 
    browser.get("http://192.168.1.1/mtenrestart.html") 
except: 
    pass
button = browser.find_element_by_name('apply') 
button.click() 

```

And here is the Bash script that controls it all, and that we call from a cronjob:

```
#!/bin/bash 
TOOLS=`dirname $0` 
# Start Selenium server 
java -jar $TOOLS/selenium-server-standalone.jar > /dev/null 2>&1 & 
SELENIUM=$! 
sleep 10 
# Reset router 
$TOOLS/restart_zyxel.py 
# Kill Selenium 
kill $SELENIUM 

```

If you find this to be of use I'd be happy to hear from you in the comments below.
