build:
	sudo docker login
	sudo docker build ./ -t lolajc/785s-messaging-automation
	sudo docker push lolajc/785s-messaging-automation
