# 785S-messaging-automation
Messaging automation using an AirCard 785S

## Prerequires  
You need an instance of AirCard Manager running on your server.

## How to use  
1. Create your config.ini based on the given example or don't forget to pass your environmenet variables when running the docker image on step 2.  

2. Build and run the docker image:  
```
docker build ./ -t messaging  
docker run -p 3000:3000 -d messaging
```

3. Send messages with the simple Flask app using an url like follows:  
http://127.0.0.1:3000/send?number=my_number&message=Hello  

## Notes
The IP and the port can be modified in the Dockerfile.  

The url and credentials of AirCard Manager can be set as environment variables or in a config file. Environment variables have priority over the config file.   
Environment variables should be named AIRCARD_URL and AIRCARD_PASSWORD. An example of a config file is provided.  
