# 785S-messaging-automation
Messaging automation using an AirCard 785S

The url and credentials of Aircard manager can be set as environment variables or in an ini file. Environment variables have priority over the config file.   
Environment variables should be named AIRCARD_URL and AIRCARD_PASSWORD. An example of a config file is provided.

The project requires a version of Chrome and chromedriver (I use Chromium and chromium-chromedriver).  

A simple Flask app is used to send a message using an url like follows:  
http://localhost:5000/send?number=my_number&message=Hello  

Work in progress
