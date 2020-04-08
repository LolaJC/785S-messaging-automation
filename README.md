# 785S-messaging-automation
Automatic sending of SMS using an AirCard 785S.

## How to use  
1. Create your config.ini based on the given example or don't forget to pass your environment variables when running the docker image on step 2.  

2. How to run with environment variables:  
```
docker run -p 3000:3000 -e "AIRCARD_URL=http://192.168.1.1" -e "AIRCARD_PASSWORD=password" -d lolajc/785s-messaging-automation
```

Or how to run with a config file:  
```
docker run -p 3000:3000 ${PWD}/config.ini:/messaging/config.ini -d lolajc/785s-messaging-automation
```

3. Send messages with the simple Flask app using an url like follows:  
http://127.0.0.1:3000/send?number=my_number&message=Hello  

## Notes
The url and credentials of AirCard Manager can be set as environment variables or in a config file. Environment variables have priority over the config file.   