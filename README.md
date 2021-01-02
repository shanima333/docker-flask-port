# Dockefile to  execute a simple flask script

Files:
- app.py
- Dockerfile
- requirements.txt

1) build image using 

docker build -t flask:new .

2) create container using 

docker container run --name demo -e FLASK_PORT=8080 -p 80:8080 flask:new

Here we can mention the FLASK port during run time
